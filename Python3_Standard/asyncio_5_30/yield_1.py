import time
from time import sleep

"""
阻塞仍然存在
把阻塞传递给上游处理
"""


def foo():
    print("foo --> 0")
    s_t = time.time()
    yield sleep, 2
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
    f = bar()
    while 1:
        try:
            x = f.send(None)
        except StopIteration as e:
            res = e.value
            break
        else:
            func, arg = x
            func(arg)
    print("task res:" + res)
    print("task --> 1")


if __name__ == '__main__':
    task()
