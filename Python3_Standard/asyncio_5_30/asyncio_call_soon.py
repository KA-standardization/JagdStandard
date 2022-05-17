import asyncio
import functools


def callback(arg, *, kwarg='Kaiser'):
    print('callback invoked with {} and {}'.format(arg, kwarg))


async def foo(loop):
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwarg='Kaiserin')
    await asyncio.sleep(0.1)
    loop.call_soon(wrapped, 2)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(foo(event_loop))
finally:
    event_loop.close()
