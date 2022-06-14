import httpx
import chardet


def autodetect(content):
    return chardet.detect(content).get("encoding")


client = httpx.Client(default_encoding=autodetect)
response = client.get("http://www.baidu.com")
print(response.encoding)
# print(response.text)
