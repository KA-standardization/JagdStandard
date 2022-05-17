import requests

# 从 Requests 2.4.0 版之后，如果系统中装了 certifi 包，Requests 会试图使用它里边的 证书

# r = requests.get('https://github.com/kennethreitz/requests/tarball/master', stream=True)

# if int(r.headers['content-length']) < 100:
#     content = r.content
#     print(content)

# print(r.iter_content(10))
# print(r.iter_lines(10))

# Requests 无法将连接释放回连接池，除非你 消耗了所有的数据，或者调用了 Response.close。
# 这样会带来连接效率低下的问题。如果你发现你在使用 stream=True 的同时还在部分读取请求的 body（或者完全没有读取 body），
# 那么你就应该考虑使用 with 语句发送请求，这样可以保证请求一定会被关闭
with requests.get('https://www.baidu.com', stream=True) as r:
    for ele in r.iter_lines():
        print(ele)

# Requests支持流式上传，这允许你发送大的数据流或文件而无需先把它们读入内存。要使用流式上传
# 用二进制模式（binary mode）打开文件。这是因为 requests 可能会为你提供 header 中的 Content-Length，在这种情况下该值会被设为文件的字节数。如果你用文本模式打开文件，就可能碰到错误
with open('massive-body') as f:
    requests.post('http://some.url/streamed', data=f)