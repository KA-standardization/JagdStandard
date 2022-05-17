import asyncio

from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future


async def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body


async def div(x, y):
    return x / y


async def good_call(a, b):
    future_ = Future()
    res = await div(a, b)
    future_.set_result(res)
    return future_


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        # res = event_loop.run_until_complete(fetch_coroutine('http://www.baidu.com'))
        # print(res.decode('utf-8'))
        ################################################################################
        res = event_loop.run_until_complete(good_call(1, 2))
        print(res.result())
    except Exception:
        pass
    finally:
        event_loop.close()
