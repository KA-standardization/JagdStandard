import array
import binascii

s = b'way down wo go'
a = array.array('b', s)
print(a)
print(binascii.hexlify(s))
print(binascii.hexlify(a))

a2 = array.array('i', range(3))
print(a2)
a2.extend(range(10))
print(a2)
print(list(enumerate(a2)))
