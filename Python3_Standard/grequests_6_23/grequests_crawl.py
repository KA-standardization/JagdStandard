import random
import string

import grequests


def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        yield base_url + ''.join(random.sample(string.ascii_lowercase, 10))


def run_experiment(base_url, num_iter=100):
    urls = generate_urls(base_url, num_iter)
    response_futures = (grequests.get(u) for u in urls)
    responses = grequests.imap(response_futures, size=100)
    for ele in responses:
        print(ele.text)


if __name__ == '__main__':
    base_url = "https://www.baidu.com/s?wd="
    run_experiment(base_url, 100)
