import sys
import struct
import binascii

# data = {'a': 100, 'b': 102, 'c': 1000}
# @ = < > !
data = [1, '我爱你中国'.encode('utf-8'), 2.2]
str_size = len(data[1])
print(str_size)

s = struct.Struct(f'I {str_size}s 1f')
pack_data = s.pack(*data)
print(s.format)
# print(s.size)
print(pack_data)
hex_data = binascii.hexlify(pack_data)
print(hex_data)
# print(sys.getsizeof(data))
# print(sys.getsizeof(pack_data))
# print(sys.getsizeof(hex_data))
#
# print('=' * 60)
# print(binascii.unhexlify(hex_data))
# unpack_data = s.unpack(binascii.unhexlify(hex_data))
# print(unpack_data)
# print(unpack_data[1].decode('utf-8'))
