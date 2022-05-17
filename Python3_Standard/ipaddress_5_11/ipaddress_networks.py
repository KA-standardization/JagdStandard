import ipaddress

NETWORKS = [
    '10.9.0.0/24',
    'fdfd:87b5:b475:5e3e::/64'
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    print(net.is_private)
    print(net.broadcast_address)
    print(net.compressed)
    print(net.with_netmask)
    print(net.with_hostmask)
    print(net.num_addresses)
    print('=' * 88)

print('=' * 88)
for n in NETWORKS:
    net = ipaddress.ip_network(n)
    for i, ip in zip(range(3), net):
        print(ip)

print('=' * 88)

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    for i, ip in zip(range(3), net.hosts()):
        print(ip)

print('=' * 88)
for n in NETWORKS:
    iface = ipaddress.ip_interface(n)
    print('{!r}'.format(iface))
    print(iface.network)
    print(iface.ip)
    print(iface.with_prefixlen)
    print(iface.with_netmask)
    print(iface.with_hostmask)
