import time
import threading
from concurrent import futures


def task(n):
    print('{}: sleeping {}'.format(threading.current_thread().name, n))
    time.sleep(n / 10)
    print('{}: done with {}'.format(threading.current_thread().name, n))
    return n / 10


ex = futures.ThreadPoolExecutor(max_workers=2)
f = ex.submit(task, 5)
print('main: future {}'.format(f))

result = f.result()
print('main: result {}'.format(result))
print('main: future affter result: {}'.format(f))
