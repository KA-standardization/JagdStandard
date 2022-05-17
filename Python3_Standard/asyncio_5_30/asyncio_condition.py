import logging
import asyncio

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] [%(thread)d] [%(threadName)-10s] [%(asctime)s] [%(name)s] [%(message)s]')


async def consumer(condition, n):
    async with condition:
        logging.debug('consumer %s is waiting', n)
        await condition.wait()
        logging.debug('consumer %s triggered', n)
    logging.debug('ending consumer %s', n)


async def manipulate_condition(condition):
    logging.debug('starting manipulate condition')

    await asyncio.sleep(0.1)

    for i in range(1, 3):
        # with await condition:
        async with condition:
            logging.debug('notifying %s consumers', i)
            condition.notify(n=i)
        await asyncio.sleep(0.1)

    async with condition:
        logging.debug('notifying remaining consumers')
        condition.notify_all()
    logging.debug('ending manipulate condition')


async def main(loop):
    condition = asyncio.Condition()
    consumers = [consumer(condition, i) for i in range(5)]
    loop.create_task(manipulate_condition(condition))

    await asyncio.wait(consumers)


event_loop = asyncio.get_event_loop()
try:
    res = event_loop.run_until_complete(main(event_loop))
    logging.debug('result %s', res)
finally:
    event_loop.close()
