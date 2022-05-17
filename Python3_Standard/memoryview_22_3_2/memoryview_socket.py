# -*- coding: utf-8 -*-
# @Time : 2022/3/7 17:52 
# @Author : Fisher
import socket

"""
socket（套接字）时这类技巧尤其有用。如你所知，当数据通过socket发送时，它不会在一次调用中发送所有数据。下面是一个简单的实现：
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
s.connect(server_address)
data = b"a" * (1024 * 100000)

"""
while data:
    sent = s.send(data)
    print(sent)
    data = data[sent:]
"""
# 零复制
mv = memoryview(data)
while mv:
    sent = s.send(mv)
    mv = mv[sent:]
