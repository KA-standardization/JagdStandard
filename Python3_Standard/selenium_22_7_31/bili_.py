import re
import time
import random
import asyncio
import datetime

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


async def foo():
    option = Options()
    # option.add_argument("--proxy-server=")
    option.add_argument("--headless")
    # http://chromedriver.storage.googleapis.com/index.html
    # web = Chrome(executable_path='./chromedriver', options=option)
    web = Chrome(executable_path='./chromedriver.exe', options=option)
    # await asyncio.sleep(random.randint(3, 10))
    web.get("https://www.bilibili.com/video/BV1EG411h7u2")
    page = web.page_source
    cnt = re.findall(re.compile('span title="总播放数(.*)" class="view item"', re.S), page)
    print("时间= {}, 播放量={}".format(datetime.datetime.now(), cnt[0]))
    await asyncio.sleep(random.randint(21, 247))
    web.quit()


def bar():
    option = Options()
    # option.add_argument("--proxy-server=")
    option.add_argument("--headless")
    # web = Chrome(executable_path='./chromedriver', options=option)
    web = Chrome(executable_path='./chromedriver.exe', options=option)
    web.get("https://www.bilibili.com/video/BV1EG411h7u2")
    page = web.page_source
    cnt = re.findall(re.compile('span title="总播放数(.*)" class="view item"', re.S), page)
    print("时间= {}, 播放量={}".format(datetime.datetime.now(), cnt[0]))
    time.sleep(random.randint(13, 240))
    web.quit()


def main():
    tasks = []
    for i in range(10):
        task = asyncio.ensure_future(foo())
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    while 1:
        try:
            # bar()
            main()
        except Exception as err:
            print(err)
