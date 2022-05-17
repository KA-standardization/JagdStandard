import time
import threading
from concurrent import futures


def task(n):
    print('{}: sleeping {}'.format(threading.current_thread().name, n))
    time.sleep(n / 10)
    print('{}: done with {}'.format(threading.current_thread().name, n))
    return n / 10


ex = futures.ThreadPoolExecutor(max_workers=2)
results = ex.map(task, range(5, 0, -1))
print('main: unprocessed results {}'.format(results))
real_results = list(results)
print('main: results: {}'.format(real_results))
