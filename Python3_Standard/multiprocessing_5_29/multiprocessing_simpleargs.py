import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG,
                    format='%(thread)d %(lineno)d %(name)s %(threadName)-s10 %(asctime)s %(levelname)s %(message)s')


# pickle 串行化
def worker(num):
    p = multiprocessing.current_process()
    logging.debug('worker %s,%s,%d', num, p.name, p.pid)


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,), name='worker-{}'.format(i))
        jobs.append(p)
        p.start()
