import base64

with open('./test.jpg', 'rb') as f:
    b_str = f.read()
    en_b64 = base64.b64encode(b_str)

print(en_b64)

with open('./test2.jpg', 'wb') as f2:
    f2.write(base64.b64decode(en_b64))
