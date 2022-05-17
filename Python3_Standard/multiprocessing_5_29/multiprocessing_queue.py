import multiprocessing


class MyFancyClass:

    def __init__(self, name):
        self.name = name

    def foo(self):
        p = multiprocessing.current_process().name
        print('in {} for {}'.format(p, self.name))


def worker(q):
    obj = q.get()
    obj.foo()


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(name='worker', target=worker, args=(queue,))
    p.start()

    queue.put(MyFancyClass('nothing is true'))

    queue.close()
    queue.join_thread()
    p.join()
