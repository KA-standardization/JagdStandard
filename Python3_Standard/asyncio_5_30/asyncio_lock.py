import asyncio
import functools


def unlock(lock):
    print('callback releasing lock')
    lock.release()


async def coroutine1(lock):
    print('coro1 waiting for the lock')
    # with await lock:
    #     print('coro1 acquired lock')
    async with lock:
        print('coro1 acquired lock')
    print('coro1 released lock')


async def coroutine2(lock):
    print('coro2 waiting for the lock')
    await lock
    try:
        print('coro2 acquired lock')
    finally:
        print('coro2 released lock')
        lock.release()


async def foo(loop):
    lock = asyncio.Lock()
    await lock.acquire()
    loop.call_later(0.1, functools.partial(unlock, lock))
    await asyncio.wait([coroutine1(lock), coroutine2(lock)])


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(foo(event_loop))
finally:
    event_loop.close()
