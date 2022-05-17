import codecs

from codecs_to_hex import to_hex

if codecs.BOM_UTF16 == codecs.BOM_UTF16_BE:
    bom = codecs.BOM_UTF16_LE
    encoding = 'utf_16_le'
else:
    bom = codecs.BOM_UTF16_BE
    encoding = 'utf_16_be'

print('Native order  :', to_hex(codecs.BOM_UTF16, 2))
print('selected order:', to_hex(bom, 2))

encoded_text = 'Jäger'.encode(encoding)
print('{:14}: {}'.format(encoding, to_hex(encoded_text, 2)))

with open('./nonnative-encoded.txt', 'wb') as f:
    f.write(bom)
    f.write(encoded_text)

print('=' * 88)

with open('./nonnative-encoded.txt', 'rb') as f:
    raw_bytes = f.read()

print('Raw   ', to_hex(raw_bytes, 2))

with codecs.open('nonnative-encoded.txt', 'r', encoding='utf-16') as f:
    decoded_text = f.read()

print('Decoded:', decoded_text)
