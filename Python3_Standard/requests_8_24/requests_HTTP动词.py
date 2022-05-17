import json

import requests
from requests.auth import HTTPBasicAuth

'''
GET、OPTIONS、HEAD、POST、PUT、PATCH、DELETE
'''
# GET
r = requests.get('https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')

r_encode_type = False
if (r.status_code == requests.codes.ok):
    print(r.headers['content-type'])
    if 'json' in r.headers['content-type']:
        r_encode_type = True

if r_encode_type:
    print(r.json())

# OPTIONS
verbs = requests.options('https://www.baidu.com')
print(verbs)
print(verbs.headers)

# POST
auth = HTTPBasicAuth('username', 'password')
body = json.dumps({'xx': True})
r = requests.post('url', data=body, auth=auth)
r = requests.post('url', json={'xx': True}, auth=auth)

# DELETE
r = requests.delete(url='', auth=auth)
r.status_code

# HEAD 请求来获取响应头
r=requests.head('',auth=auth)
