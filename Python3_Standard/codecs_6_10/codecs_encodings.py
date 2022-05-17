import unicodedata

from codecs_to_hex import to_hex

text = 'Jäger'

for ch in text:
    print('  {!r}: {}'.format(ch, unicodedata.name(ch, ch)))

print('UTF-8: {!r}'.format(to_hex(text.encode('utf-8'), 1)))
print('UTF-16: {!r}'.format(to_hex(text.encode('utf-16'), 2)))

