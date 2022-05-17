import asyncio


async def coroutine():
    print('in coroutine')
    return 'Kaiser'


event_loop = asyncio.get_event_loop()

try:
    return_value = event_loop.run_until_complete(coroutine())
    print(return_value)
finally:
    event_loop.close()
