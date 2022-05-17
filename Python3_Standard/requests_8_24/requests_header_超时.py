import requests

'''
连接超时指的是在你的客户端实现到远端机器端口的连接时（对应的是`connect()`_），
Request 会等待的秒数。
一个很好的实践方法是把连接超时设为比 3 的倍数略大的一个数值，因为 TCP 数据包重传窗口 (TCP packet retransmission window) 的默认大小是 3

r = requests.get('https://github.com', timeout=5)
r = requests.get('https://github.com', timeout=(3.05, 27))
如果远端服务器很慢，你可以让 Request 永远等待
r = requests.get('https://github.com', timeout=None)
'''
