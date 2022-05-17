import time
import random
import logging
import operator
import threading

logging.basicConfig(level=logging.DEBUG, format='[%(threadName)-10s] %(message)s')


class Counter:

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquire lock')
            self.value = self.value + 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = operator.truediv(random.randint(1, 5), 10)
        logging.debug('Sleeping %0.2f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')


counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()

logging.debug('Counter %d', counter.value)
