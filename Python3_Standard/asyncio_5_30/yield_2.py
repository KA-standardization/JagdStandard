import time
from time import sleep

"""
阻塞仍然存在
把阻塞传递给上游处理
"""


class YieldFrom(object):

    def __init__(self, obj):
        self.value = obj

    def __iter__(self):
        yield self


class Task(object):
    def __init__(self, core):
        self.core = core

    def run(self):
        while 1:
            try:
                x = self.core.send(None)
            except StopIteration as e:
                res = e.value
                break
            else:
                assert isinstance(x, YieldFrom)
                func, arg = x.value
                func(arg)
        print("task res: " + res)


def foo():
    print("foo --> 0")
    s_t = time.time()
    # yield sleep, 2
    yield YieldFrom((sleep, 2))
    assert time.time() - s_t, "sleep is not run"
    print("foo --> 1")
    return "协程结果"


def bar():
    print("bar --> 0")
    res = yield from foo()
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


def task():
    print("task --> 0")
    res = yield from bar()
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
    t = Task(task())
    t.run()
    print(time.time() - time_s)
