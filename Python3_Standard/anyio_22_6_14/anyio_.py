import httpx
import anyio

import time
#
s_t = time.time()

async def main():
    urls = [
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
        "https://www.baidu.com/s?wd=Fisher",
        "https://www.baidu.com/s?wd=d",
        "https://www.baidu.com/s?wd=c",
        "https://www.baidu.com/s?wd=g",
        "https://www.baidu.com/s?wd=h",
        "https://www.baidu.com/s?wd=j",
        "https://www.baidu.com/s?wd=k",
        "https://www.baidu.com/s?wd=l",
        "https://www.baidu.com/s?wd=p",
        "https://www.baidu.com/s?wd=u",
    ]
    async with httpx.AsyncClient() as client:
        # g = (len(client.get(item).text) for item in urls)
        # print(list(g))
        for item in urls:
            response = await client.get(item)
            # print(response.text)
            print(len(response.text))


anyio.run(main, backend='trio')

# urls = [
#     "https://www.baidu.com/s?wd=Fisher",
#     "https://www.baidu.com/s?wd=d",
#     "https://www.baidu.com/s?wd=c",
#     "https://www.baidu.com/s?wd=g",
#     "https://www.baidu.com/s?wd=h",
#     "https://www.baidu.com/s?wd=j",
#     "https://www.baidu.com/s?wd=k",
#     "https://www.baidu.com/s?wd=l",
#     "https://www.baidu.com/s?wd=p",
#     "https://www.baidu.com/s?wd=u",
# ]
#
# for item in urls:
#     res = httpx.get(item)
#     print(len(res.text))

print(time.time() - s_t)
