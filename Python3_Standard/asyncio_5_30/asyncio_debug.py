import sys
import time
import logging
import asyncio
import warnings
import argparse

parser = argparse.ArgumentParser('debugging asyncio')
parser.add_argument('-v', dest='verbose', default=False, action='store_true', )
args = parser.parse_args()

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s]: %(message)s', stream=sys.stderr)
LOG = logging.getLogger('')


async def inner():
    LOG.info('inner starting')
    time.sleep(0.1)
    LOG.info('inner completed')


async def outer(loop):
    LOG.info('outer starting')
    await asyncio.ensure_future(loop.create_task(inner()))
    LOG.info('outer completed')


event_loop = asyncio.get_event_loop()
if args.verbose:
    LOG.info('enabling debugging')

    event_loop.set_debug(True)

    event_loop.slow_callback_duration = 0.001

    warnings.simplefilter('always', ResourceWarning)

LOG.info('entering event loop')
event_loop.run_until_complete(outer(event_loop))
