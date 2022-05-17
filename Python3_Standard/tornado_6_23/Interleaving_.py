import random
import string
import asyncio

from tornado.gen import convert_yielded
from tornado import gen, ioloop
from tornado.concurrent import Future


def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        yield base_url + ''.join(random.sample(string.ascii_lowercase, 10))


async def get_():
    # fetch_future = convert_yielded(next(urls))
    urls = ['http://www.baidu.com/s?wd=bbbb'], ['http://www.baidu.com/s?wd=aaaa']
    fetch_future = convert_yielded(urls)
    print(fetch_future)
    yield fetch_future
    # while True:
    #     chunk = yield fetch_future
    #
    #     if chunk is None: break
    #     # future_.set_result(chunk)
    #     print(chunk)
    #     fetch_future = convert_yielded(next(urls))


if __name__ == '__main__':
    # base_url = "https://www.baidu.com/s?wd="
    # # urls = generate_urls(base_url, 10)
    urls = ['http://www.baidu.com/s?wd=bbbb'], ['http://www.baidu.com/s?wd=aaaa']
    event_loop = asyncio.get_event_loop()
    try:
        res = event_loop.run_until_complete(get_())
    finally:
        event_loop.close()
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(get_)


