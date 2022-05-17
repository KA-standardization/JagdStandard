import asyncio


async def phase(i):
    print('in phase {}'.format(i))
    # await asyncio.sleep(0.5 - (0.1 * i))
    await asyncio.sleep(0.1 * i)
    print('done with phase {}'.format(i))
    return 'phase {} result'.format(i)


async def foo(num_phases):
    print('starting foo')
    phases = [phase(i) for i in range(num_phases)]
    res = []
    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print('received answer {!r}'.format(answer))
        res.append(answer)
    print('results: {!r}'.format(res))
    return res


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(foo(3))
finally:
    event_loop.close()
