import time
import threading


def worker():
    '''
    thread worker function
    :return:
    '''
    print('worker')


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

print('=' * 88)


def worker2(i):
    '''
    thread worker function
    :return:
    '''
    print('worker--{}'.format(i))


threads = []
for i in range(5):
    t = threading.Thread(target=worker2, args=(i,))
    threads.append(t)
    t.start()

print('=' * 88)


def worker3():
    print(threading.current_thread().getName(), 'starting')
    time.sleep(1)
    print(threading.current_thread().getName(), 'ending')


def my_server():
    print(threading.current_thread().getName(), 'starting')
    time.sleep(1)
    print(threading.current_thread().getName(), 'ending')


t = threading.Thread(name='t', target=my_server)
w = threading.Thread(name='t2', target=worker3)
w2 = threading.Thread(target=worker3)

t.start()
w.start()
w2.start()
