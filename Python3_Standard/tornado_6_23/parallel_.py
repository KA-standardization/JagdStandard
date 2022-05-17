import asyncio

from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
from tornado.gen import multi


async def parallel_fetch(urls):
    http_client = AsyncHTTPClient()
    future_ = Future()
    try:
        resources = await multi({url: http_client.fetch(url) for url in urls})
        future_.set_result(resources)
    except Exception:
        pass
    return future_


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    urls = ['http://www.baidu.com/s?wd=bbbb', 'http://www.baidu.com/s?wd=aaaa', 'http://www.baidu.com/s?wd=cccc',
            'http://www.baidu.com/s?wd=dddd', 'http://www.baidu.com/s?wd=eeee','http://www.gooleeeeeee.com/']
    try:
        res = event_loop.run_until_complete(parallel_fetch(urls))
        for val in res.result().values():
            print(val.body.decode())
    except Exception as e:
        print(e)
        pass
    finally:
        event_loop.close()
