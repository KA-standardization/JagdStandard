import sys
import logging
import asyncio

MESSAGES = ['Nothing is ture'.encode('utf-8'), 'The Kaiser and The Kaiserin'.encode('utf-8'), 'Jagd'.encode('utf-8')]

SERVER_ADDRESS = ('localhost', 10001)

logging.basicConfig(level=logging.DEBUG, format='%(name)s %(message)s', stream=sys.stderr)
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()


async def echo_client(address, messages):
    log = logging.getLogger('echo_client')
    log.debug('connecting to {} port {}'.format(*address))
    reader, writer = await asyncio.open_connection(*address)
    for msg in messages:
        writer.write(msg)
        log.debug('sending {!r}'.format(msg))
    if writer.can_write_eof():
        writer.write_eof()
    await writer.drain()

    log.debug('waiting for response')
    while True:
        data = await reader.read(128)
        if data:
            log.debug('received {!r}'.format(data))
        else:
            log.debug('closing')
            writer.close()
            return


try:
    event_loop.run_until_complete(echo_client(SERVER_ADDRESS, MESSAGES))
finally:
    log.debug('closing event loop')
    event_loop.close()
