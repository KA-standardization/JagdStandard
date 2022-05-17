import math
import functools

import grequests


class AsyncBatcher(object):
    # __slots__ = ['batch_size', 'batch', "save", "flush"]

    def __init__(self, batch_size):
        self.batch_size = batch_size
        self.batch = []

    def save(self, prime):
        url = f"https://www.baidu.com/s?wd={prime}"
        self.batch.append((url, prime))
        if len(self.batch) == self.batch_size:
            self.flush()

    def flush(self):
        responses_futures = (grequests.get(url) for url, _ in self.batch)
        responses = grequests.map(responses_futures)
        for res, (url, prime) in zip(responses, self.batch):
            # print('{}-->({}, {})'.format(res, url, prime))
            finish_save_prime(res, prime)
        self.batch = []


def finish_save_prime(response, prime):
    if response.status_code != 200:
        print("Error saving prime: {}".format(prime))
    else:
        print(response.text)


def check_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def calculate_primes_async(max_size):
    barcher = AsyncBatcher(100)
    for num in range(max_size):
        barcher.save(num)
    barcher.flush()
    return


if __name__ == '__main__':
    calculate_primes_async(1000)
