import random
import string
import functools

from tornado import ioloop
from tornado.httpclient import AsyncHTTPClient
from tornado import gen

# AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient", max_clients=100)
AsyncHTTPClient.configurable_base()


def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        yield base_url + ''.join(random.sample(string.ascii_lowercase, 10))


@gen.coroutine
def run_experiment(base_url, num_iter=100):
    http_client = AsyncHTTPClient()
    urls = generate_urls(base_url, num_iter)
    responses = yield [http_client.fetch(url) for url in urls]
    for ele in responses:
        print(ele)
    res_sum = sum(len(r.body) for r in responses)
    # return res_sum
    raise gen.Return(value=res_sum)


if __name__ == '__main__':
    base_url = "https://www.baidu.com/s?wd="
    _ioloop = ioloop.IOLoop.instance()
    run_func = functools.partial(run_experiment, base_url, 100)
    res = _ioloop.run_sync(run_func)
    print(res)
