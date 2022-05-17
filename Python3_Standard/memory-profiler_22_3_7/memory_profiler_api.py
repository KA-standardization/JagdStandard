# -*- coding: utf-8 -*-
# @Time : 2022/3/7 16:41 
# @Author : Fisher

from memory_profiler import memory_usage


def f(a, n=100):
    import time
    time.sleep(2)
    b = [a] * n
    time.sleep(1)
    return b


if __name__ == '__main__':
    # 获取 Python 函数的内存消耗，那么您应该在元组(f, args, kw)中指定函数及其参数
    print(memory_usage((f, (1,), {'n': int(1e6)})))
