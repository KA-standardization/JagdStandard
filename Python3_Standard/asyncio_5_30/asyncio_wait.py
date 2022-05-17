import asyncio


async def phase(i):
    print('in phase {}'.format(i))
    await asyncio.sleep(0.1 * i)
    print('done with phase {}'.format(i))
    return 'phase {} result'.format(i)


async def foo(num_phases):
    print('starting foo')
    phases = [phase(i) for i in range(num_phases)]
    print('waiting for phases to complete')
    # wait 返回 已完成 未完成
    complete, pending = await asyncio.wait(phases)
    results = [t.result() for t in complete]
    print('results: {!r}'.format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(foo(3))
finally:
    event_loop.close()
