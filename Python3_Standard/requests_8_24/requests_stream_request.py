import json

import requests

r = requests.get('http://httpbin.org/stream/20', stream=True)

'''
当使用 decode_unicode=True 在 Response.iter_lines() 或 Response.iter_content() 中时，
你需要提供一个回退编码方式，以防服务器没有提供默认回退编码，从而导致错误
'''
if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    if line:
        print(json.loads(line))
