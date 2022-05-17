import codecs

text = 'Jäger'

# strict replace ignore xmlcharrefreplace backslashreplace
try:
    with codecs.open('encode_error.txt', 'w', encoding='ascii', errors='replace') as f:
        f.write(text)
except UnicodeEncodeError as err:
    print('Error:', err)

else:
    with open('encode_error.txt', 'rb') as f:
        print('File contents: {!r}'.format(f.read()))
