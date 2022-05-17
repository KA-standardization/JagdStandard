import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] [%(threadName)-10s] %(message)s')


def worker(barrier):
    logging.debug('waiting for barrier with %s other', barrier.n_waiting)
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        logging.debug('aborting')
    else:
        logging.debug('after barrier %s', worker_id)


NUM_THREAD = 3
barrier = threading.Barrier(NUM_THREAD + 1)

threads = [threading.Thread(name='worker-%s' % i, target=worker, args=(barrier,)) for i in range(NUM_THREAD)]
for t in threads:
    logging.debug('starting')
    t.start()
    time.sleep(0.1)

barrier.abort()

for t in threads:
    t.join()
