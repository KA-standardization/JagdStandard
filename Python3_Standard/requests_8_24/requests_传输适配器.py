import ssl

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import requests

# 指定的 SSL 版本

'''
Requests 开发团队刻意指定了内部库（urllib3）的默认 SSL 版本。一般情况下这样做没有问题，
不过是不是你可能会需要连接到一个服务节点，而该节点使用了和默认不同的 SSL 版本
'''


# 告诉 urllib3 让它使用 SSLv3
class Ssl3HttpAdapter(HTTPAdapter):
    """"Transport adapter" that allows us to use SSLv3."""

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_SSLv3)

s = requests.Session()
s.mount('http://www.github.com', Ssl3HttpAdapter())
