import asyncio


async def phase(i):
    print('in phase {}'.format(i))
    try:
        await asyncio.sleep(0.1 * i)
    except asyncio.CancelledError:
        print('phase {} canceled'.format(i))
        raise
    else:
        print('done with phase {}'.format(i))
        return 'phase {} result'.format(i)


async def foo(num_phases):
    print('starting foo')
    phases = [phase(i) for i in range(num_phases)]
    print('waiting 0.1 for phases to complete')
    # complete, pending = await asyncio.wait(phases, timeout=0.1)
    complete, pending = await asyncio.wait(phases, timeout=1)
    if pending:
        print('canceling task')
        for t in pending:
            t.cancel()
    if complete:
        res = [tk.result() for tk in complete]
        print('res: {!r}'.format(res))
    print('exit foo')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(foo(3))
finally:
    event_loop.close()
