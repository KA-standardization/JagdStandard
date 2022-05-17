import sys
import socket
import struct
import binascii

for string_address in ['192.168.1.1', '127.0.0.1']:
    packed = socket.inet_aton(string_address)
    print(packed)
    print(string_address)
    print(binascii.hexlify(packed))
    print(socket.inet_ntoa(packed))
    print()

print('=' * 88)
str_address = '2002:ac10:10a:1344:21e:52ff:fe77:44a'
packed = socket.inet_pton(socket.AF_INET6, str_address)
print(str_address)
print(packed)
print(binascii.hexlify(packed))
print(socket.inet_ntop(socket.AF_INET6, packed))
