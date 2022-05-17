import pathlib

f = pathlib.Path('test.txt')
f.write_bytes('hello world'.encode('utf-8'))
with f.open('r', encoding='utf-8') as handle:
    print(handle.read())

print('=' * 88)
print(f.read_text('utf-8'))


