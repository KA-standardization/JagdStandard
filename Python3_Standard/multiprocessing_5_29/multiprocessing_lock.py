import sys
import multiprocessing


def worker_with(lock, stream):
    with lock:
        stream.write('Lock acquired via with\n')


def worker_no_with(lock, stream):
    lock.acquired()
    try:
        stream.write('Lock acquired directly\n')
    finally:
        lock.release()


lk = multiprocessing.Lock()
w = multiprocessing.Process(target=worker_with, args=(lk, sys.stdout))
nw = multiprocessing.Process(target=worker_no_with, args=(lk, sys.stdout))

w.start()
nw.start()
w.join()
nw.join()
