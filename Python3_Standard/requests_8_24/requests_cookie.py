import requests

url = 'http://www.baidu.com'
# r = requests.get(url)
jar = requests.cookies.RequestsCookieJar()
jar.set('BD_UPN', '12314753', domain='baidu.com', path='/cookies')
jar.set('BIDUPSID', 'AD605F5C85CE4E080DC4CBC09B522021', domain='baidu.com', path='/elsewhere')
r = requests.get(url, cookies=jar)
print(r.text)
print(r.cookies['BDORZ'])

for ele in r.cookies:
    print(ele)
