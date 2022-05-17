from gevent import monkey

monkey.patch_socket()

import time
import gevent
import string
import random
import requests

from gevent._semaphore import Semaphore


def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        yield base_url + ''.join(random.sample(string.ascii_lowercase, 10))


def chunked_requests(urls, chunk_size=100):
    semaphore = Semaphore(chunk_size)
    requests = [gevent.spawn(download, u, semaphore) for u in urls]
    for response in gevent.iwait(requests):
        yield response


def download(url, semaphoree):
    with semaphoree:
        res = requests.get(url)
        return res


def run_experiment(base_url, num_iter=500):
    # urls = generate_urls(base_url, num_iter)
    urls=['http://www.baidu.com/s?wd=bbbb', 'http://www.baidu.com/s?wd=aaaa', 'http://www.baidu.com/s?wd=cccc',
            'http://www.baidu.com/s?wd=dddd', 'http://www.baidu.com/s?wd=eeee','http://www.gooleeeeeee.com/']
    response_futures = chunked_requests(urls, 100)
    for ele in response_futures:
        if ele.value:
            print(ele.value.text)
        else:
            print('NNNNNNNNNNNNNN')


    response_size = sum(r.value for r in response_futures)
    return response_size


if __name__ == '__main__':
    # delay = 100
    # num_iter = 500
    # base_url = "http://www.baidu.com/s?wd={}"
    #
    # start = time.time()
    # result = run_experiment(base_url, num_iter)
    # end = time.time()
    #
    # print("Result: {}, Time: {}".format(result, end - start))

    import gevent
    import greenlet
    print(gevent.__version__)
    print(greenlet.__version__)
