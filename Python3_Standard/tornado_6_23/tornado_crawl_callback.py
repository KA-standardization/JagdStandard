import random
import string
import functools

from tornado import ioloop
from tornado.httpclient import AsyncHTTPClient

# AsyncHTTPClient.configure()
AsyncHTTPClient.configurable_base()


def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        yield base_url + ''.join(random.sample(string.ascii_lowercase, 10))


def fetch_urls(urls, callback):
    http_client = AsyncHTTPClient()
    urls = list(urls)
    responses = []

    def _finish_getch_urls(result):
        responses.append(result)
        print(responses)
        if len(responses) == len(urls):
            callback(responses)

    for url in urls:
        # yield http_client.fetch(url, callback=_finish_getch_urls)
        http_client.fetch(url, callback=_finish_getch_urls)


def run_experiment(base_url, num_iter=500, callback=None):
    urls = generate_urls(base_url, num_iter)
    callback_passthrou = functools.partial(_finish_run_experiment, callback)
    fetch_urls(urls, callback_passthrou)


def _finish_run_experiment(responses, callback):
    print(list(responses))
    # res_sum = sum(len(r.body) for r in responses)
    # print(res_sum)
    callback()


if __name__ == '__main__':
    base_url = "https://www.baidu.com/s?wd="
    _ioloop = ioloop.IOLoop.instance()
    _ioloop.add_callback(run_experiment, base_url, 100, _ioloop.stop)

    _ioloop.start()
