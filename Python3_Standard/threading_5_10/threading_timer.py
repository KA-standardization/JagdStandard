import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='[%(threadName)-10s] %(message)s')


def delayed():
    logging.debug('worker running')


t1 = threading.Timer(interval=0.3, function=delayed)
t1.setName('t1')
t2 = threading.Timer(interval=0.3, function=delayed)
t2.setName('t2')

logging.debug('starting times')
t1.start()
t2.start()

logging.debug('waiting before canceling %s', t2.getName())
time.sleep(0.2)
logging.debug('canceling %s', t2.getName())
t2.cancel()
logging.debug('done')
