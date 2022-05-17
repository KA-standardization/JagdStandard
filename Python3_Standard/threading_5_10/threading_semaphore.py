import time
import random
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(threadName)-10s] %(message)s')


class ActivePoll:

    def __init__(self):
        super(ActivePoll, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running %s', self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running %s', self.active)


def worker(s, pool):
    logging.debug('waiting to join the pool')
    with s:
        name = threading.current_thread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)


pool = ActivePoll()
s = threading.Semaphore(2)
for i in range(4):
    t = threading.Thread(target=worker, name='worker-%d' % i, args=(s, pool))
    t.start()
