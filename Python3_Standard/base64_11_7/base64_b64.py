import base64
import textwrap

# with open(__file__, 'r', encoding='utf-8') as f:
#     raw = f.read()
b_str = 'this is test bas64 file.'.encode('utf-8')
print(b_str)
en_b64 = base64.b64encode(b_str)
n_str = len(b_str)
padding = 3 - (n_str % 3)
print('{} bytes before encoding'.format(n_str), 'expect {} padding bytes'.format(padding),
      '{} bytes after encoding'.format(len(en_b64)), sep='\n')
print(en_b64)
print('=' * 88)
# 查看输入中的各个24位序列（3字节），然后将这24位编码为输出中的4个字节
de_b64 = base64.b64decode(en_b64)
print(de_b64)

print('=' * 88)
en_with_pluses = b'\xfb\xef'
en_with_slashes = b'\xff\xff'
print(en_with_pluses, base64.standard_b64encode(en_with_pluses), base64.urlsafe_b64encode(en_with_pluses), sep='\n')
print(en_with_slashes, base64.standard_b64encode(en_with_slashes), base64.urlsafe_b64encode(en_with_slashes), sep='\n')
print('=' * 88)
# base32 ASCII集中26个大写字母及数字2-7
print(base64.b32encode(b_str), base64.b32decode(base64.b32encode(b_str)), sep='\n')

print('='*88)
# base16处理16进制字母表
# 编码位数下降时，采用编码格式的输出就会占用更多空间
print(base64.b16encode(b_str), base64.b16decode(base64.b16encode(b_str)), sep='\n')

print('='*88)
# base85使用一个扩展的字母表，在空间上更节省
# Git使用版本 b85
print(base64.b85encode(b_str), base64.b85decode(base64.b85encode(b_str)), sep='\n')
# PDF使用版本 a85
print(base64.a85encode(b_str), base64.a85decode(base64.a85encode(b_str)), sep='\n')