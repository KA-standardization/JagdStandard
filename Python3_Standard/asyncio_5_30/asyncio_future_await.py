import asyncio


def mark_done(future, result):
    print('setting future result to {!r}'.format(result))
    future.set_result(result)


async def foo(loop):
    all_done = asyncio.Future()
    loop.call_soon(mark_done, all_done, 'Kaiser')
    res = await all_done
    print('res: {!r}'.format(res))


event_loop = asyncio.get_event_loop()
try:
    # event_loop.run_until_complete(foo(event_loop))
    res2 = event_loop.run_until_complete(foo(event_loop))
    # None
    print('res2 {}'.format(res2))
finally:
    event_loop.close()
