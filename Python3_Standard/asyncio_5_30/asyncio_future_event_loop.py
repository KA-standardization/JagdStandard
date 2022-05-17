import asyncio


def mark_done(future, result):
    print('setting future to {!r}'.format(result))
    future.set_result(result)


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()
    event_loop.call_soon(mark_done, all_done, 'Kaiser')
    res = event_loop.run_until_complete(all_done)
    print(res)
finally:
    event_loop.close()
