#include "network_interface.hh"

#include "arp_message.hh"
#include "ethernet_frame.hh"

#include <iostream>

// Dummy implementation of a network interface
// Translates from {IP datagram, next hop address} to link-layer frame, and from link-layer frame to IP datagram

// For Lab 5, please replace with a real implementation that passes the
// automated checks run by `make check_lab5`.

// You will need to add private members to the class declaration in `network_interface.hh`

using namespace std;

//! \param[in] ethernet_address Ethernet (what ARP calls "hardware") address of the interface
//! \param[in] ip_address IP (what ARP calls "protocol") address of the interface
NetworkInterface::NetworkInterface(const EthernetAddress &ethernet_address, const Address &ip_address)
    : _ethernet_address(ethernet_address), _ip_address(ip_address) {
    cerr << "DEBUG: Network interface has Ethernet address " << to_string(_ethernet_address) << " and IP address "
         << ip_address.ip() << "\n";
}

//! \param[in] dgram the IPv4 datagram to be sent
//! \param[in] next_hop the IP address of the interface to send it to (typically a router or default gateway, but may also be another host if directly connected to the same network as the destination)
//! (Note: the Address type can be converted to a uint32_t (raw 32-bit IP address) with the Address::ipv4_numeric() method.)
void NetworkInterface::send_datagram(const InternetDatagram &dgram, const Address &next_hop) {
    // convert IP address of next hop to raw 32-bit representation (used in ARP header)
    const uint32_t next_hop_ip = next_hop.ipv4_numeric();
    if (!map_.count(next_hop_ip)) {
        send_arp(ETHERNET_BROADCAST, next_hop_ip, ARPMessage::OPCODE_REQUEST);
        wait_queue_.push(wait_queue_entity{dgram, next_hop});
        return;
    }
    if (clock_ms_ - map_ms_[next_hop_ip] > 30000) {
        // expire, resend arp
        send_arp(ETHERNET_BROADCAST, next_hop_ip, ARPMessage::OPCODE_REQUEST);
        wait_queue_.push(wait_queue_entity{dgram, next_hop});
        return;
    }

    EthernetFrame frame;
    frame.header().src = _ethernet_address;
    frame.header().dst = map_.find(next_hop_ip)->second;
    frame.header().type = EthernetHeader::TYPE_IPv4;
    frame.payload() = dgram.serialize();
    _frames_out.push(frame);
}

//! \param[in] frame the incoming Ethernet frame
optional<InternetDatagram> NetworkInterface::recv_frame(const EthernetFrame &frame) {
    if (frame.header().dst != _ethernet_address && frame.header().dst != ETHERNET_BROADCAST) {
        return nullopt;
    }
    if (frame.header().type == EthernetHeader::TYPE_IPv4) {
        InternetDatagram datagram;
        if (datagram.parse(frame.payload()) != ParseResult::NoError) {
            return nullopt;
        }
        return datagram;
    } else if (frame.header().type == EthernetHeader::TYPE_ARP) {
        ARPMessage arp;
        if (arp.parse(frame.payload()) != ParseResult::NoError) {
            return nullopt;
        }
        if (arp.opcode == ARPMessage::OPCODE_REQUEST) {
            map_[arp.sender_ip_address] = arp.sender_ethernet_address;
            map_ms_[arp.sender_ip_address] = clock_ms_;

            if (arp.target_ip_address != _ip_address.ipv4_numeric()) {
                return nullopt;
            }
            send_arp(arp.sender_ethernet_address, arp.sender_ip_address, ARPMessage::OPCODE_REPLY);
        } else if (arp.opcode == ARPMessage::OPCODE_REPLY) {
            map_[arp.sender_ip_address] = arp.sender_ethernet_address;
            map_ms_[arp.sender_ip_address] = clock_ms_;
        }
        for (size_t i = 0; i < wait_queue_.size(); i++) {
            wait_queue_entity tmp = wait_queue_.front();
            wait_queue_.pop();
            send_datagram(tmp.dgram, tmp.next_hop);
        }
        return nullopt;
    }
    return nullopt;
}

//! \param[in] ms_since_last_tick the number of milliseconds since the last call to this method
void NetworkInterface::tick(const size_t ms_since_last_tick) { clock_ms_ += ms_since_last_tick; }

void NetworkInterface::send_arp(EthernetAddress dst, uint32_t dst_ip, uint16_t opcode) {
    // check is already send in last five seconds.
    auto iter = map_last_time_ms_.find(dst_ip);
    if (iter != map_last_time_ms_.end()) {
        if (clock_ms_ - iter->second < 5000) {
            return;
        }
    }
    EthernetFrame frame;
    frame.header().type = EthernetHeader::TYPE_ARP;
    frame.header().src = _ethernet_address;
    frame.header().dst = dst;

    ARPMessage arp;
    arp.sender_ip_address = _ip_address.ipv4_numeric();
    arp.sender_ethernet_address = _ethernet_address;
    arp.target_ip_address = dst_ip;
    arp.opcode = opcode;
    if (arp.opcode == ARPMessage::OPCODE_REPLY) {
        arp.target_ethernet_address = dst;
    }

    frame.payload() = arp.serialize();

    map_last_time_ms_[dst_ip] = clock_ms_;
    _frames_out.push(frame);
}
