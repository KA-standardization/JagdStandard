import binascii
import ipaddress

ADDRESSES = [
    '10.0.17.100',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:12aa'
]
for ip in ADDRESSES:
    addr = ipaddress.ip_address(ip)
    print('{!r}'.format(addr))
    print('version', addr.version)
    print('private', addr.is_private)
    print('packed from', binascii.hexlify(addr.packed))
    print('integer',int(addr))