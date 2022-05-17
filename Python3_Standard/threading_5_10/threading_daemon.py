import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s %(message)s)')


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Ending')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Ending')


d = threading.Thread(name='daemon', target=daemon, daemon=True)
t = threading.Thread(name='non-daemon', target=non_daemon)

print(threading.current_thread().getName())

d.start()
t.start()

d.join(0.3)
print('daemon is alive--{}'.format(d.is_alive()))
t.join()
