import sys
import logging
import asyncio

SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s')

logger = logging.getLogger('main')
event_loop = asyncio.get_event_loop()


class EchoServer(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log = logging.getLogger('EchoServer_{}_{}'.format(*self.address))
        self.log.debug('connection accepted')

    def data_received(self, data):
        self.log.debug('received {!r}'.format(data))
        self.transport.write(data)
        self.log.debug('send {!r}'.format(data))

    def eof_received(self):
        self.log.debug('received EOF')
        if self.transport.can_write_eof():
            self.transport.write_eof()

    def connection_lost(self, err):
        if err:
            self.log.error('ERROR: {}'.format(err))
        else:
            self.log.debug('closing')
        super().connection_lost(err)


factory = event_loop.create_server(EchoServer, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
logger.debug('starting up on {} port {}'.format(*SERVER_ADDRESS))

try:
    event_loop.run_forever()
finally:
    logger.debug('closing server')
    event_loop.run_until_complete(server.wait_closed())
    logger.debug('closing event loop')
    event_loop.close()
