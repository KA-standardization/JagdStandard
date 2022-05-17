import time
import random
import logging
import operator
import threading

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s %(message)s)')


def worker():
    pause = operator.truediv(random.randint(1, 5), 10)
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')


for i in range(3):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

main_thread = threading.main_thread()

for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()
