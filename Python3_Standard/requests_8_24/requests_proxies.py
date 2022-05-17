import requests

'''
import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

requests.get("http://example.org", proxies=proxies)

你也可以通过环境变量 HTTP_PROXY 和 HTTPS_PROXY 来配置代理。
$ export HTTP_PROXY="http://10.10.1.10:3128"
$ export HTTPS_PROXY="http://10.10.1.10:1080"

$ python
>>> import requests
>>> requests.get("http://example.org")

若你的代理需要使用HTTP Basic Auth，可以使用 http://user:password@host/ 语法
proxies = {
    "http": "http://user:pass@10.10.1.10:3128/",
}

Request 还支持 SOCKS 协议的代理
pip install requests[socks]
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}
'''