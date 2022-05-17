import io

output = io.BytesIO()
wrapper = io.TextIOWrapper(output, encoding='utf-8', write_through=True)
wrapper.write('hello')
wrapper.write('world')
print(output.getvalue())
output.close()
print('=' * 88)
input = io.BytesIO('aaaaaa'.encode('utf-8'))
wrapper = io.TextIOWrapper(input, encoding='utf-8')
print(wrapper.read())
