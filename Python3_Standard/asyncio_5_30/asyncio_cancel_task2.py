import asyncio


async def task_func():
    print('in task func sleeping')
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('task func was canceled')
        raise
    return 'The Kaiser'


def task_canceller(t):
    print('in task canceller')
    t.cancel()
    print('canceled the task')


async def foo(loop):
    task = loop.create_task(task_func())
    loop.call_soon(task_canceller, task)
    try:
        await task
    except asyncio.CancelledError:
        print('foo also sees task as canceled')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(foo(event_loop))
finally:
    event_loop.close()
