import asyncio


async def outer():
    print('in outer')
    print('waiting for res1')
    res1 = await phase1()
    print('waiting res2')
    res2 = await phase2(res1)
    return (res1, res2)


async def phase1():
    print('in phase1')
    return 'res111'


async def phase2(arg):
    print('in phase2')
    return 'res222 derived from {}'.format(arg)


event_loop = asyncio.get_event_loop()

try:
    return_value = event_loop.run_until_complete(outer())
    print(return_value)
finally:
    event_loop.close()
