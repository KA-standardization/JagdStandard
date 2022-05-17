import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] [%(threadName)-10s] %(message)s')


def consumer(cond):
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available consumer')


def producer(cond):
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()


cond = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(cond,))
c2 = threading.Thread(name='c2', target=consumer, args=(cond,))
p = threading.Thread(name='p', target=producer, args=(cond,))
c1.start()
time.sleep(0.2)
c2.start()
time.sleep(0.2)
p.start()
