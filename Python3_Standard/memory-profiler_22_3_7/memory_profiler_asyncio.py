# -*- coding: utf-8 -*-
# @Time : 2022/3/7 17:01 
# @Author : Fisher
import asyncio

from memory_profiler import profile


@profile
@asyncio.coroutine
def foo():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    yield from asyncio.sleep(1)
    del b
    return a


if __name__ == "__main__":
    # python -m memory_profiler memory_profiler_asyncio.py
    loop = asyncio.get_event_loop()
    loop.run_until_complete(foo())
