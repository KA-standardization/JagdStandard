import time
from concurrent import futures


def task(n):
    print('{}: starting'.format(n))
    raise ValueError('the value {} is no good'.format(n))


ex = futures.ThreadPoolExecutor(max_workers=2)
f = ex.submit(task, 5)

error = f.exception()
print('main: error {}'.format(error))

try:
    result = f.result()
except ValueError as err:
    print('main: saw error {} when accessing result'.format(err))
