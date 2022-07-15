import time
import asyncio

import requests
import threading


class Foo(object):

    def __init__(self, url):
        self.url = url

    def request(self):
        res = requests.get(self.url)
        time.sleep(1)
        print(len(res.text))

    def __await__(self):
        threading.Thread(target=self.request).start()


def request(url, future):
    res = len(requests.get(url).text)
    time.sleep(1)
    future.set_result(res)


async def parse(url, loop):
    all_done = loop.create_future()
    await asyncio.threads.to_thread(request, url=url, future=all_done)
    print('setting future to {!r}'.format(all_done.result()))


if __name__ == '__main__':
    urls = 'http://www.baidu.com'

    tasks = []
    s = time.time()

    loop = asyncio.get_event_loop()
    for i in range(20):
        task = asyncio.ensure_future(parse(urls, loop))
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))

    print(time.time() - s)
