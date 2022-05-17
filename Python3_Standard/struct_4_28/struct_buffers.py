import array
import ctypes
import struct
import binascii

data = (1, 'aa'.encode('utf-8'), 2.7)
s = struct.Struct('= I 2s f')
print(s.size)
c = ctypes.create_string_buffer(s.size)
print(c.raw)
print(binascii.hexlify(c.raw))
s.pack_into(c, 0, *data)
print(binascii.hexlify(c.raw))
print(s.unpack_from(c, 0))

print('=' * 88)

a = array.array('b', b'\0' * s.size)
print(binascii.hexlify(a))
s.pack_into(a, 0, *data)
print(binascii.hexlify(a))
print(s.unpack_from(a, 0))
