import io

output = io.StringIO()
output.write('hello world')
print(output.getvalue())
output.close()
print('=' * 88)
input = io.StringIO('hello world2')
print(input.read())

