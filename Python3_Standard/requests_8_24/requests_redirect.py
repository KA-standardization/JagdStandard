import requests

r=requests.get('http://github.com')
print(r.status_code)
print(r.history)
# for ele in r.history:
#     print(ele)

# 禁用重定向
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)

print(r.history)

#
requests.get('http://github.com', timeout=0.001)