import io

output = io.BytesIO()
output.write('hello world'.encode('utf-8'))
output.write('Äüö'.encode('utf-8'))

print(output.getvalue())
output.close()
print('=' * 88)
input = io.BytesIO('hello'.encode('utf-8'))
print(input.read())
