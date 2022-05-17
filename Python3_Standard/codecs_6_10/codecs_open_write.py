import sys
import codecs

from codecs_to_hex import to_hex

print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())

encoding = 'utf-8'
with codecs.open('./text.txt', mode='w', encoding=encoding) as f:
    f.write('Jäger')

nbytes = {
    'utf-8': 1,
    'utf-16': 2,
    'utf-32': 4,
}.get(encoding, 1)

with open('./text.txt', 'rb') as f:
    print(to_hex(f.read(), nbytes))
