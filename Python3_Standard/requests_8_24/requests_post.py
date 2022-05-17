import json
import requests

# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}

# r = requests.post(url, data=json.dumps(payload))
# r = requests.post(url, json=payload)
# print(r.text)

########################################################################################################################
# url = 'http://httpbin.org/post'
# files = {'file': open('aaa.mp4', 'rb')}
# 显式地设置文件名，文件类型和请求头
# files = {'file': ('bbbb.mp4', open('aaa.mp4', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
# r = requests.post(url, files=files)
# print(r.text)

########################################################################################################################
# url = 'http://httpbin.org/post'
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
#
# r = requests.post(url, files=files)
# print(r.status_code)
# print(requests.codes.ok)
# print(r.text)
########################################################################################################################
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.headers)
# if bad_r.status_code >=400:
#     bad_r.raise_for_status()

