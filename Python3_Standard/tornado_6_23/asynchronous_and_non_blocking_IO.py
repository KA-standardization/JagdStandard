import asyncio
from tornado.httpclient import HTTPClient, AsyncHTTPClient
from tornado.concurrent import Future


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


async def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body


def async_fetch_manual(url):
    http_client = AsyncHTTPClient()
    future_a = Future()
    fetch_future = http_client.fetch(url)

    def on_fetch(f):
        future_a.set_result(f.result().body)

    fetch_future.add_done_callback(on_fetch)
    return future_a


if __name__ == '__main__':
    # res = synchronous_fetch('http://www.baidu.com')
    # print(res)

    ###########################################################################################

    # event_loop = asyncio.get_event_loop()
    # try:
    #     res = event_loop.run_until_complete(asynchronous_fetch('http://www.baidu.com'))
    #     print(res.decode('utf-8'))
    # finally:
    #     event_loop.close()

    ############################################################################################
    event_loop = asyncio.get_event_loop()
    try:
        res = event_loop.run_until_complete(async_fetch_manual('http://www.baidu.com'))
        print(res.decode('utf-8'))
    finally:
        event_loop.close()
