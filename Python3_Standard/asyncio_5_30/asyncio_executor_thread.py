import sys
import time
import logging
import asyncio
import concurrent.futures


def blocks(n):
    log = logging.getLogger('blocks {}'.format(n))
    log.info('running')
    time.sleep(0.1)
    log.info('done')
    return n ** 2


async def run_blocking_tasks(executor):
    log = logging.getLogger('run blocking tasks')
    log.info('starting')

    log.info('create executor tasks')
    loop = asyncio.get_event_loop()
    blocking_tasks = [loop.run_in_executor(executor, blocks, i) for i in range(6)]

    log.info('waiting for executor tasks')
    completed, penging = await asyncio.wait(blocking_tasks)
    results = [t.result() for t in completed]
    log.info('results: {!r}'.format(results))

    log.info('exiting')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] [%(threadName)10s] [%(name)18s] [%(message)s]',
                        stream=sys.stderr)

    excutor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(run_blocking_tasks(excutor))
    finally:
        event_loop.close()
