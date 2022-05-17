import requests

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "cookie": "MONITOR_WEB_ID=67ce5798-1ddd-4908-90f3-9317cd539d8a",
    "origin": "https://www.douyin.com",
    "pragma": "no-cache",
    "referer": "https://www.douyin.com/",
    "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
}


def download(url):
    with requests.get(url, headers=headers, stream=True) as r:
        with open('aaa.mp4', 'wb')as f:
            for i in r.iter_content(chunk_size=1024):
                f.write(i)


if __name__ == '__main__':
    url = 'https://v26-web.douyinvod.com/ae6dec99ec08dffdfc3243835a9dc071/6124ae3d/video/tos/cn/tos-cn-ve-15/2ad6c40ae4e14b008dd7f151babb9e5a/?a=6383&br=2178&bt=2178&cd=0%7C0%7C0&ch=26&cr=0&cs=0&dr=0&ds=3&er=&ft=0J.120FFckag3&l=021629790249346fdbd400a040000000a705308000000032aa86e&lr=all&mime_type=video_mp4&net=0&pl=0&qs=0&rc=M3I4aWQ6ZmY7NzMzNGkzM0ApZjVkZTNpNGRnNzg3Njo8Z2debjBgcjRvM2ZgLS1kLS9zc15gLWI0X2NiNjUwYDNhNTY6Yw%3D%3D&vl=&vr='
    download(url)
