import io
import codecs

buffer = io.StringIO()

# base-64 bzip2 rot-13 zip
stream = codecs.getwriter('rot-13')(buffer)

text = 'abcdefg'

stream.write(text)
stream.flush()

print('Original:', text)
print('ROT-13', buffer.getvalue())


