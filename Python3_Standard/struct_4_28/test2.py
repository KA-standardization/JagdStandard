import struct
import binascii

data = 'xing-zi-ling-1'.encode('utf-8')
str_size = len(data)
print(str_size)
s = struct.Struct(f'{str_size}s')
print(s.format)
pack_data = s.pack(data)
print(pack_data)
hex_data = binascii.hexlify(pack_data)
print(hex_data)
