import collections
import heapq
import itertools
import random
import time
from time import sleep

"""
阻塞仍然存在
把阻塞传递给上游处理
"""


class EventLoop(object):

    def __init__(self):
        self.ready = collections.deque()
        self.scheduled = []
        self.stop_ = False

    def call_soon(self, callbak, *args):
        self.ready.append((callbak, args))

    def call_later(self, delay, callbak, *args):
        t = time.time() + delay
        heapq.heappush(self.scheduled, (t, callbak, args))

    def run(self):
        while 1:
            self._run()
            if self.stop_:
                break

    def _run(self):
        t = time.time()
        if self.scheduled:
            if self.scheduled[0][0] < t:
                _, func, arg = heapq.heappop(self.scheduled)
                self.ready.append((func, arg))

        task_num = len(self.ready)
        for i in range(task_num):
            func, arg = self.ready.popleft()
            func(*arg)

    def stop(self):
        self.stop_ = True


class YieldFrom(object):

    def __init__(self, obj):
        self.value = obj

    def __await__(self):
        yield self


class Task(object):
    def __init__(self, core):
        self.core = core
        self.flag = False
        self.res = None
        self._id = "TID-{}".format(next(t_id))

    def run(self):
        print("T ID --> {}".format(self._id))
        if not self.flag:
            try:
                x = self.core.send(None)
            except StopIteration as e:
                self.res = e.value
                self.flag = True
            else:
                assert isinstance(x, YieldFrom)

                loop.call_later(x.value, self.run)
                # func, arg = x.value
                # func(arg)
        # print("task res: " + self.res)


async def foo():
    print("foo --> 0")
    s_t = time.time()

    s_r = random.random()
    # yield sleep, 2
    # await YieldFrom((sleep, 2))
    await YieldFrom(s_r)
    assert time.time() - s_t, "sleep is not run"
    print("foo --> 1")
    return "协程结果"


async def bar():
    print("bar --> 0")
    res = await foo()
    # f = foo()
    # while 1:
    #     try:
    #         x = f.send(None)
    #     except StopIteration as e:
    #         res = e.value
    #         break
    #     else:
    #         yield x
    print("bar -- 1")
    return "中间处理" + res


async def task():
    print("task --> 0")
    res = await bar()
    # f = bar()
    # while 1:
    #     try:
    #         x = f.send(None)
    #     except StopIteration as e:
    #         res = e.value
    #         break
    #     else:
    #         func, arg = x
    #         func(arg)
    # print("task res:" + res)
    print("task --> 1")
    return "task" + res


if __name__ == '__main__':
    time_s = time.time()
    t_id = itertools.count(1)
    loop = EventLoop()
    for i in range(10):
        t = Task(task())
        loop.call_soon(t.run)
    # loop.call_later(2, t.run)
    loop.call_later(2.1, loop.stop)
    loop.run()
    # t.run()
    # # do something
    # for i in range(2):
    #     print(i)
    #     time.sleep(0.5)
    # t.run()
    print(time.time() - time_s)
