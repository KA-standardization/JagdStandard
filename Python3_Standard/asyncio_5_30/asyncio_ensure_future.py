import asyncio


async def wrapped():
    print('wrapped')
    return 'Kaiser'


async def inner(task):
    print('inner: starting')
    print('inner: waiting for {!r}'.format(task))
    res = await task
    print('inner: task returned {!r}'.format(res))


async def starter():
    print('starter: create task')
    task = asyncio.ensure_future(wrapped())
    print('starter: waiting for inner')
    # 对于 ensure future 的协程 在使用await之前这个协程不会启动
    await inner(task)
    print('starter: inner returned')


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    res = event_loop.run_until_complete(starter())
finally:
    event_loop.close()
