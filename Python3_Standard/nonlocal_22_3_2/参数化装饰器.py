# -*- coding: utf-8 -*-
# @Time : 2022/3/8 12:55 
# @Author : Fisher
import time

DEFAULT_FMT = "[{elapsed:0.8f}s] {name} ({args}) --> {res}"


def clock(fmt=DEFAULT_FMT):
    def foo(func):
        def bar(*_args):
            t0 = time.time()
            _res = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ", ".join(repr(arg) for arg in _args)
            res = repr(_res)
            print(locals())
            print(fmt.format(**locals()))
            return _res

        return bar

    return foo


if __name__ == '__main__':
    @clock()
    def snooze(s):
        time.sleep(s)


    for i in range(3):
        snooze(i / 10)
