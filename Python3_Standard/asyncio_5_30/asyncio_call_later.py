import asyncio


def callback(n):
    print('callback {} invoked'.format(n))


async def foo(loop):
    loop.call_later(0.2, callback, 'a')
    loop.call_later(0.1, callback, 'b')
    loop.call_soon(callback, 'c')

    # await asyncio.sleep(0.1)
    await asyncio.sleep(0.3)


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(foo(event_loop))
finally:
    event_loop.close()
