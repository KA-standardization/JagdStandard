import requests

# 开启SSL验证
r = requests.get('https://github.com', verify=True)
print(r.text)

# 可以为 verify 传入 CA_BUNDLE 文件的路径，或者包含可信任 CA 证书文件的文件夹路径
r = requests.get('https://github.com', verify='/path/to/certfile')

# 将其保持在会话中 如果 verify 设为文件夹路径，文件夹必须通过 OpenSSL 提供的 c_rehash 工具处理
s = requests.Session()
s.verify = '/path/to/certfile'

# 你也可以指定一个本地证书用作客户端证书，可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组
# 本地证书的私有 key 必须是解密状态。目前，Requests 不支持使用加密的 key
r = requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))
print(r.request.headers)

# 保持在会话中
s = requests.Session()
s.cert = '/path/client.cert'


'''
请求默认支持 SSL 验证。但是，它依赖于用户使用包含主机名的 URL 发出请求。但是，如果用户需要使用 IP 地址发出请求，他们实际上无法根据他们想要请求的主机名验证证书

import requests
from requests_toolbelt.adapters import host_header_ssl
s = requests.Session()
s.mount('https://', host_header_ssl.HostHeaderSSLAdapter())
s.get("https://93.184.216.34", headers={"Host": "example.org"})
'''
