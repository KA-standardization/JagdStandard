# -*- coding: utf-8 -*-
# @Time : 2022/3/7 16:44 
# @Author : Fisher
from memory_profiler import profile

f = open('mem.log', 'w+')


@profile(stream=f)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


@profile(stream=f)
def my_func1():
    a = [2] * (10 ** 6)
    b = [3] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    # python -m memory_profiler memory_profiler_REPORTING.py
    my_func()
    my_func1()
