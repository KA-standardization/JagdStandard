import binascii

s = 'xing-zi-ling-1'.encode('utf-8')
s2 = binascii.hexlify(s)
print(s2)
s3 = int(s2, 16)
print(s3)
s4 = str(hex(s3))
s4 = s4[2:].encode('utf-8')

data = binascii.unhexlify(s4).decode('utf-8')
print(data)
