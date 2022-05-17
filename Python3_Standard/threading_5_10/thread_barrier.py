import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] [%(threadName)-10s] %(message)s')


def worker(barrier):
    logging.debug('waiting for barrier with %s', barrier.n_waiting)
    worker_id = barrier.wait()
    logging.debug('after barrier %s', worker_id)


NUM_THREADS = 3
barrier = threading.Barrier(NUM_THREADS)
threads = [threading.Thread(name='worker-%s' % i, target=worker, args=(barrier,)) for i in range(NUM_THREADS)]

for t in threads:
    logging.debug('Starting')
    t.start()
    time.sleep(0.1)

for t in threads:
    t.join()
