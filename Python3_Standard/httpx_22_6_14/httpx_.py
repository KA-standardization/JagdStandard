import httpx

url = "http://www.baidu.com"
res = httpx.get(url)
print(res.status_code)
print(res.headers['date'])

# print(res.text)
"""
params = {'key1': 'value1', 'key2': ['value2', 'value3']}
URL('https://httpbin.org/get?key1=value1&key2=value2&key2=value3')
params = {'key1': 'value1', 'key2': 'value2'}
r = httpx.get('https://httpbin.org/get', params=params)
r.json()
"""
