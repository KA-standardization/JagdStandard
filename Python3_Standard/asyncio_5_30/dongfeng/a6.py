import time
import asyncio

import requests


def request(url, future):
    res = len(requests.get(url).text)
    future.set_result(res)


async def parse(url, loop):
    all_done = asyncio.Future()
    await asyncio.threads.to_thread(request, url=url, future=all_done)
    print('setting future to {!r}'.format(all_done.result()))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    urls = 'http://www.baidu.com'

    tasks = []
    s = time.time()

    for i in range(10):
        task = asyncio.ensure_future(parse(urls, loop))
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))

    print(time.time() - s)
