import time

from scapy.all import *

if __name__ == '__main__':
    ####################################################################################################################
    """    
    https://scapy.readthedocs.io/en/latest/usage.html#interactivetutorial
    第7层构造,DNS查询
    """
    # p = sr1(IP(dst='114.114.114.114') / UDP() / DNS(rd=1, qd=DNSQR(qname="zhihu.com")))
    # print(p.show())

    ####################################################################################################################
    # p2 = sr1(IP(dst='10.0.17.100') / ICMP())
    ####################################################################################################################
    # p3 = sr1(IP(dst='112.80.248.76') / TCP(dport=22, flags='S'))
    # print(p3.show())
    ####################################################################################################################
    # ans, uans = sr(IP(dst='10.0.17.100') / ICMP())
    # print(ans.show())
    # for item in ans:
    #     print(item)
    ####################################################################################################################
    """
    # 捕获数据包
    """
    # a = sniff(filter='host 103.41.167.234', count=5)
    # time.sleep(15)
    # print(a.show())
    ####################################################################################################################
    """
    TCP端口扫描
    """
    # b = sr1(IP(dst='10.0.17.100') / TCP(dport=22, flags='S'))
    # print(b.show())
    # ans,uans = sr(IP(dst='10.0.17.100') / TCP(dport=(22, 120), flags='S'))
    # for item in ans:
    #     print(item)
    ####################################################################################################################
    """
    TCP端口扫描目标网络
    """
    # ans, uans = sr(IP(dst='10.0.17.100/24') / TCP(dport=22, flags='S'))
    # for item in ans:
    #     print(item)
    ####################################################################################################################
    """
    伪造IP头,长度为2,IP版本为3
    """
    # send(IP(dst='10.0.17.200', ihl=2, version=3) / ICMP())
    # send(fragment(IP(dst='10.0.17.200')/ICMP()/("AAA"*60000)))
    ####################################################################################################################
    """
    send()函数将在第3层发送数据包 sendp()函数将在第2层工作
    """
    # send(IP(dst='10.0.17.200') / ICMP())
    # sendp(Ether() / IP(dst='10.0.17.200', ttl=(1, 4)), iface='Intel(R) Ethernet Connection (7) I219-V')
    """
    tcpreplay
    """
    # sendp(rdpcap('./pcaps/a.pcap'))
    """
    如果return_packets=True作为参数传递，send()和sendp()也将返回发送的包列表
    """
    # p = send(IP(dst='10.0.17.200'), return_packets=True)
    # print(p.show())
    ####################################################################################################################
    """
    函数fuzz()能够更改任何默认值，这些默认值不是由一个对象计算出来的(如校验和)，该对象的值是随机的，其类型适合该字段。这使得快速构建模糊模板并在循环中发送它们成为可能。
    以IP层正常，UDP层和NTP层模糊为例。UDP校验和将是正确的，UDP目的端口将被NTP重载为123,NTP版本将被迫为4。所有其他端口将被随机化。
    注意:如果你在IP层使用fuzz()， src和dst参数将不是随机的，所以为了做到这一点，使用RandIP()
    """
    # p = send(IP(dst='10.0.17.200') / fuzz(UDP() / NTP(version=4)), loop=1, return_packets=True)
    # print(p.show())
    ####################################################################################################################
    """
    注入不合适的值
    """
    # pkt = IP(len=RawVal(b"aaaaa"), src='127.0.0.1')
    # print(bytes(pkt))
    ####################################################################################################################
    """
    sr()函数用于发送数据包和接收应答。该函数返回两个包和答案，以及未回答的包。
    函数sr1()是一个变体，它只返回一个应答发送的包(或包集)的包。数据包必须是三层数据包(IP、ARP等)。
    srp()函数对第2层数据包(Ethernet、802.3等)执行相同的操作。如果没有响应，则在超时时将分配一个None值。
    """
    # p = sr1(IP(dst='www.baidu.com') / ICMP() / "XXXXXXXXXXXX")
    # print(p.show())
    ####################################################################################################################
    """
    inter参数指定两个报文之间等待的时间间隔(以秒为单位)
    如果retry为-3,Scapy将重新发送未答复的数据包，直到连续3次对同一组未答复的数据包没有更多的答案。
    timeout参数指定发送最后一个报文后等待的时间
    """
    # ans, uans = sr(IP(dst="10.0.17.200") / TCP(dport=[21, 22, 23]), inter=0.5, retry=-2, timeout=1)
    # ans.summary(lfilter=lambda s, r: r.sprintf("%TCP.flags%") == "SA",
    #             prn=lambda s, r: r.sprintf("%TCP.sport% is open"))
    # for item in ans:
    #     print(item)
    ####################################################################################################################
    """
    SYN
    dport=(100,1000) 100-1000
    dport=[100,1000] 100, 1000
    sport=RandShort()
    """
    # p = sr1(IP(dst="10.0.17.200") / TCP(dport=80, flags="S"))
    # print(p.show())
    ####################################################################################################################
    # ans, unans = sr(IP(dst=["10.0.17.100", "10.0.17.101", "10.0.17.200"]) / TCP(dport=[22, 80, 443], flags="S"))
    # ans.make_table(lambda s, r: (s.dst, s.dport, r.sprintf("{TCP:%TCP.flags%}{ICMP:%IP.src% - %ICMP.type%}")))
    """
    只显示设置了“SA”标志的数据包
    """
    # ans.nsummary(lfilter=lambda s, r: r.sprintf("%TCP.flags%") == "SA")
    """
    指示哪些端口是打开的
    """
    # ans.summary(lfilter=lambda s, r: r.sprintf("%TCP.flags%") == "SA",
    #             prn=lambda s, r: r.sprintf("%TCP.sport% is open"))
    # ans.filter(lambda s, r: TCP in r and r[TCP].flags & 2).make_table(lambda s, r:
    #                                                                   (s.dst, s.dport, "X"))
    ####################################################################################################################
    """
    report_ports()函数，它不仅可以自动进行SYN扫描，还可以生成一个收集结果的LaTeX输出
    """
    # p = report_ports("10.0.17.200", (22, 9100))
    # p = report_ports("10.0.17.200", [22, 9100])
    # print(p)
    ####################################################################################################################
    """
    print(lsc())
            sr               : Send and receive packets at layer 3
            sr1              : Send packets at layer 3 and return only the first answer
            srp              : Send and receive packets at layer 2
            srp1             : Send and receive packets at layer 2 and return only the first answer
            srloop           : Send a packet at layer 3 in loop and print the answer each time
            srploop          : Send a packet at layer 2 in loop and print the answer each time
            sniff            : Sniff packets
            p0f              : Passive OS fingerprinting: which OS emitted this TCP SYN ?
            arpcachepoison   : Poison target's cache with (your MAC,victim's IP) couple
            send             : Send packets at layer 3
            sendp            : Send packets at layer 2
            traceroute       : Instant TCP traceroute
            arping           : Send ARP who-has requests to determine which hosts are up
            ls               : List  available layers, or infos on a given layer
            lsc              : List user commands
            queso            : Queso OS fingerprinting
            nmap_fp          : nmap fingerprinting
            report_ports     : portscan a target and output a LaTeX table
            dyndns_add       : Send a DNS add message to a nameserver for "name" to have a new "rdata"
            dyndns_del       : Send a DNS delete message to a nameserver for "name"
        IPID_count          : Identify IP id values classes in a list of packets
        arpcachepoison      : Poison target's cache with (your MAC,victim's IP) couple
        arping              : Send ARP who-has requests to determine which hosts are up
        arpleak             : Exploit ARP leak flaws, like NetBSD-SA2017-002.
        bind_layers         : Bind 2 layers on some specific fields' values.
        bridge_and_sniff    : Forward traffic between interfaces if1 and if2, sniff and return
        chexdump            : Build a per byte hexadecimal representation
        computeNIGroupAddr  : Compute the NI group Address. Can take a FQDN as input parameter
        corrupt_bits        : 
        corrupt_bytes       : 
        defrag              : defrag(plist) -> ([not fragmented], [defragmented],
        defragment          : defragment(plist) -> plist defragmented as much as possible 
        dhcp_request        : Send a DHCP discover request and return the answer
        dyndns_add          : Send a DNS add message to a nameserver for "name" to have a new "rdata"
        dyndns_del          : Send a DNS delete message to a nameserver for "name"
        etherleak           : Exploit Etherleak flaw
        explore             : Function used to discover the Scapy layers and protocols.
        fletcher16_checkbytes: Calculates the Fletcher-16 checkbytes returned as 2 byte binary-string.
        fletcher16_checksum : Calculates Fletcher-16 checksum of the given buffer.
        fragleak            : --
        fragleak2           : --
        fragment            : Fragment a big IP datagram
        fuzz                : 
        getmacbyip          : Return MAC address corresponding to a given IP address
        getmacbyip6         : Returns the MAC address corresponding to an IPv6 address
        hexdiff             : 
        hexdump             : Build a tcpdump like hexadecimal view
        hexedit             : Run hexedit on a list of packets, then return the edited packets.
        hexstr              : Build a fancy tcpdump like hex from bytes.
        import_hexcap       : Imports a tcpdump like hexadecimal view
        is_promisc          : Try to guess if target is in Promisc mode. The target is provided by its ip.
        linehexdump         : Build an equivalent view of hexdump() on a single line
        ls                  : List  available layers, or infos on a given layer class or name.
        neighsol            : Sends and receive an ICMPv6 Neighbor Solicitation message
        overlap_frag        : Build overlapping fragments to bypass NIPS
        promiscping         : Send ARP who-has requests to determine which hosts are in promiscuous mode
        rdpcap              : Read a pcap or pcapng file and return a packet list
        report_ports        : portscan a target and output a LaTeX table
        restart             : Restarts scapy
        rfc                 : 
        send                : 
        sendp               : 
        sendpfast           : Send packets at layer 2 using tcpreplay for performance
        sniff               : 
        split_layers        : Split 2 layers previously bound.
        sr                  : 
        sr1                 : 
        sr1flood            : Flood and receive packets at layer 3 and return only the first answer
        srbt                : send and receive using a bluetooth socket
        srbt1               : send and receive 1 packet using a bluetooth socket
        srflood             : Flood and receive packets at layer 3
        srloop              : 
        srp                 : 
        srp1                : 
        srp1flood           : Flood and receive packets at layer 2 and return only the first answer
        srpflood            : Flood and receive packets at layer 2
        srploop             : 
        tcpdump             : Run tcpdump or tshark on a list of packets.
        tdecode             : 
        traceroute          : Instant TCP traceroute
        traceroute6         : Instant TCP traceroute using IPv6
        traceroute_map      : Util function to call traceroute on multiple targets, then
        tshark              : Sniff packets and print them calling pkt.summary().
        wireshark           : 
        wrpcap              : Write a list of packets to a pcap file
    """
    # ans, unans = sr(IP(dst='10.0.17.200', ttl=(4, 25), id=RandShort()) / TCP(flags=0x2))
    # for snd, rcv in ans:
    #     print(snd.ttl, rcv.src, isinstance(rcv.payload, TCP))
    ####################################################################################################################
    """
    GeoIP2
        pip install geoip2
        pip install cartopy
            pip install Pillow
            pip install pyshp
            pip install Shapely
            pip install pyproj
            pip install geos
            pip install P:\install\Cartopy-0.20.2-cp310-cp310-win_amd64.whl
    """
    # import geoip2
    # import cartopy
    # conf.geoip_city='path/to/GeoLite2-City.mmdb'
    # # a = traceroute(["www.baidu.com", "www.python.org"], verbose=0)
    # # a.world_trace()
    # traceroute_map(["www.baidu.com", "www.python.org"])
    ####################################################################################################################
    #Asynchronous Sniffing
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
