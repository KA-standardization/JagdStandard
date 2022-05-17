import asyncio
import functools


def callback(future, n):
    print('{} future done: {}'.format(n, future.result()))


async def register_callback(all_done):
    print('register callback on future')
    all_done.add_done_callback(functools.partial(callback, n='A'))
    all_done.add_done_callback(functools.partial(callback, n='B'))


async def foo(all_done):
    await register_callback(all_done)
    all_done.set_result('the result')


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()
    event_loop.run_until_complete(foo(all_done))
finally:
    event_loop.close()
