import requests

# 该响应对象包含服务器返回的所有信息，也包含你原来创建的 Request 对象。如下是一个简单的请求

r = requests.get('https://m.baidu.com')
# 服务器返回给我们的响应头部信息
print(r.headers)
# 发送到服务器的请求的头部
print(r.request.headers)

'''
from requests import Request, Session

s = Session()
req = Request('GET', url,
    data=data,
    headers=header
)
prepped = req.prepare()

# do something with prepped.body
# do something with prepped.headers

resp = s.send(prepped,
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout
)

print(resp.status_code)

上述代码会失去 Requests Session 对象的一些优势， 尤其 Session 级别的状态，例如 cookie 就不会被应用到你的请求上去。要获取一个带有状态的 PreparedRequest， 请用 Session.prepare_request() 取代 Request.prepare() 的调用
from requests import Request, Session

s = Session()
req = Request('GET',  url,
    data=data
    headers=headers
)

prepped = s.prepare_request(req)

# do something with prepped.body
# do something with prepped.headers

resp = s.send(prepped,
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout
)

print(resp.status_code)
'''