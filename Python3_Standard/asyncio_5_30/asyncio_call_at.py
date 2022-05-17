import time
import asyncio
import functools


def callback(n, loop, kwarg='Kaiser'):
    print('callback {} invoked at {}|kwarg: {}'.format(n, loop.time(), kwarg))


async def foo(loop):
    now = loop.time()
    print('clock time: {}'.format(time.time()))
    print('loop time {}'.format(now))
    loop.call_at(now + 0.2, callback, 'A', loop)
    wrapped = functools.partial(callback, kwarg='Kaiserin')
    loop.call_at(now + 0.1, wrapped, 'B', loop)
    loop.call_soon(callback, 'C', loop)
    loop.call_later(0.3, callback, 'D', loop)

    await asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(foo(event_loop))
finally:
    event_loop.close()
