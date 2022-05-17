import array
import binascii


def to_hex(a):
    chars_per_item = a.itemsize * 2
    hex_version = binascii.hexlify(a)
    num_chunks = len(hex_version)
    print('  {}'.format(num_chunks))
    for i in range(num_chunks):
        start = i * chars_per_item
        end = start + chars_per_item
        print('   {}'.format(hex_version))
        yield hex_version[start:end]


start = int('0x12345678', 16)
end = start + 5
a1 = array.array('i', range(start, end))
a2 = array.array('i', range(start, end))
print(a2)
a2.byteswap()
print(a2)
fmt = '{!r:>12} {:>12} {!r:>12} {:>12}'
for values in zip(to_hex(a1), a1, to_hex(a2), a2):
    print(fmt.format(*values))
