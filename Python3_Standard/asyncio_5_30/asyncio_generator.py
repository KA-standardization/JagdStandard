import asyncio


@asyncio.coroutine
def phase1():
    print('in phase1')
    return 'res1'


@asyncio.coroutine
def phase2(arg):
    print('in phase2')
    return 'res2 {}'.format(arg)


@asyncio.coroutine
def outer():
    print('in outer')
    print('waiting for res1')
    res1 = yield from phase1()
    print('waiting for res2')
    res2 = yield from phase2(res1)
    return (res1, res2)


event_loop = asyncio.get_event_loop()

try:
    res = event_loop.run_until_complete(outer())
    print(res)
finally:
    event_loop.close()
