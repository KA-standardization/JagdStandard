import collections
import heapq
import itertools
import random
import threading
import time
from time import sleep

import requests

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


class Future(object):

    def __init__(self):
        global loop
        self.res = None
        self.flag = False
        self.callbaks = []
        self._loop=loop

    def set_res(self, result):
        if self.flag:
            raise RuntimeError("res is not done")
        self.res = result
        self.flag = True
        for item in self.callbaks:
            # item()
            self._loop.call_soon(item)

    def get_res(self):
        if self.flag:
            return self.res
        else:
            raise RuntimeError("res is not done")

    def set_done_callbak(self, callbak):
        self.callbaks.append(callbak)

    def __await__(self):
        yield self
        return self.get_res()


class Task(Future):
    def __init__(self, core):
        super().__init__()
        self.core = core
        # self.flag = False
        # self.res = None
        self._id = "TID-{}".format(next(t_id))
        self._loop.call_soon(self.run)

    def run(self):
        print("T ID --> {}".format(self._id))
        if not self.flag:
            try:
                x = self.core.send(None)
            except StopIteration as e:
                self.set_res(e.value)
                # self.res = e.value
                # self.flag = True
            else:
                assert isinstance(x, Future)

                x.set_done_callbak(self.run)

                # loop.call_later(x.value, self.run)
                # func, arg = x.value
                # func(arg)
        print("task: {} res: ".format(self._id) + str(self.res))


async def foo():
    global loop
    print("foo --> 0")
    # s_t = time.time()
    #
    # s_r = random.random()
    # yield sleep, 2
    # await YieldFrom((sleep, 2))
    f = Future()
    # loop.call_later(random.random(), f.set_res, "Le Beau")
    requests_baidu(f)

    res = await f
    # assert time.time() - s_t, "sleep is not run"
    # print("foo --> 1")
    return res


def requests_baidu(fut):
    def request():
        r = requests.get("https://www.baidu.com")
        r_code = r.status_code
        fut.set_res(r_code)
        time.sleep(0.5)

    threading.Thread(target=request).start()


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
    return "中间处理" + str(res)


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
    for i in range(20):
        t = Task(task())
        # loop.call_soon(t.run)
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

    """
    await coroutine function
    yield from generator function
    """
