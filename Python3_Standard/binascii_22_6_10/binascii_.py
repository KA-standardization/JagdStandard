import binascii

s = b"POST"
print(binascii.b2a_hex(s))
print(binascii.b2a_base64(s))
