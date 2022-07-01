#include "router.hh"

#include <iostream>

using namespace std;

// Dummy implementation of an IP router

// Given an incoming Internet datagram, the router decides
// (1) which interface to send it out on, and
// (2) what next hop address to send it to.

// For Lab 6, please replace with a real implementation that passes the
// automated checks run by `make check_lab6`.

// You will need to add private members to the class declaration in `router.hh`

//! \param[in] route_prefix The "up-to-32-bit" IPv4 address prefix to match the datagram's destination address against
//! \param[in] prefix_length For this route to be applicable, how many high-order (most-significant) bits of the route_prefix will need to match the corresponding bits of the datagram's destination address?
//! \param[in] next_hop The IP address of the next hop. Will be empty if the network is directly attached to the router (in which case, the next hop address should be the datagram's final destination).
//! \param[in] interface_num The index of the interface to send the datagram out on.
void Router::add_route(const uint32_t route_prefix,
                       const uint8_t prefix_length,
                       const optional<Address> next_hop,
                       const size_t interface_num) {
    cerr << "DEBUG: adding route " << Address::from_ipv4_numeric(route_prefix).ip() << "/" << int(prefix_length)
         << " => " << (next_hop.has_value() ? next_hop->ip() : "(direct)") << " on interface " << interface_num << "\n";

    route_table_.push_back(Table{route_prefix, prefix_length, next_hop, interface_num});
}

//! \param[in] dgram The datagram to be routed
void Router::route_one_datagram(InternetDatagram &dgram) {
    size_t target_interface = 0;
    uint8_t longest = 0;
    bool is_find = false;
    for (auto table : route_table_) {
        if (table.prefix_length_ >= longest) {
            uint32_t mask = table.prefix_length_ == 0 ? 0 : 0xFFFFFFFF << (32 - table.prefix_length_);
            if ((dgram.header().dst & mask) == table.route_prefix_) {
                is_find = true;
                longest = table.prefix_length_;
                target_interface = table.interface_num_;
            }
        }
    }

    if (!is_find || dgram.header().ttl <= 1) {
        return;
    }

    dgram.header().ttl--;

    if (route_table_[target_interface].next_hop_.has_value()) {
        interface(target_interface).send_datagram(dgram, route_table_[target_interface].next_hop_.value());
    } else {
        interface(target_interface).send_datagram(dgram, Address::from_ipv4_numeric(dgram.header().dst));
    }
}

void Router::route() {
    // Go through all the interfaces, and route every incoming datagram to its proper outgoing interface.
    for (auto &interface : _interfaces) {
        auto &queue = interface.datagrams_out();
        while (not queue.empty()) {
            route_one_datagram(queue.front());
            queue.pop();
        }
    }
}
