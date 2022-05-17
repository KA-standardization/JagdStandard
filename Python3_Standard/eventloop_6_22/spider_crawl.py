import time
import string
import random
import requests
import inspect


def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))


print(inspect.isgeneratorfunction(generate_urls))


def run_experiment(base_url, num_iter=100):
    response_size = 0
    for i, url in enumerate(generate_urls(base_url, num_iter)):
        print(i, url)
    #     res = requests.get(url)
    #     response_size += len(res.text)
    # return response_size


if __name__ == '__main__':
    delay = 100
    num_iter = 500
    base_url = "http://127.0.0.1:8080/add?name=serial&delay={}&".format(delay)

    start = time.time()
    result = run_experiment(base_url, num_iter)
    end = time.time()

    print("Result: {}, Time: {}".format(result, end - start))
