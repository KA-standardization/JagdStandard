import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')


def worker():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


t = threading.Thread(name='worker', target=worker)
t.start()
