import sys
import queue
import select
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address),
      file=sys.stderr)
server.bind(server_address)

server.listen(5)

message_queues = {}

TIMEOUT = 1000

READ_ONLY = (
    select.POLLIN |
    select.POLLPRI |
    select.POLLHUP |
    select.POLLERR
)
READ_WRITE = READ_ONLY | select.POLLOUT

poller = select.poll()
poller.register(server, READ_ONLY)

fd_to_socket = {
    server.fileno(): server,
}

while True:
    print('waiting for the next event', file=sys.stderr)
    events = poller.poll(TIMEOUT)

    for fd, flag in events:

        s = fd_to_socket[fd]

        if flag & (select.POLLIN | select.POLLPRI):

            if s is server:
                connection, client_address = s.accept()
                print('  connection', client_address,
                      file=sys.stderr)
                connection.setblocking(0)
                fd_to_socket[connection.fileno()] = connection
                poller.register(connection, READ_ONLY)

                message_queues[connection] = queue.Queue()

            else:
                data = s.recv(1024)
                if data:
                    print('  received {!r} from {}'.format(
                        data, s.getpeername()), file=sys.stderr,
                    )
                    message_queues[s].put(data)
                    poller.modify(s, READ_WRITE)

                else:
                    print('  closing', client_address,
                          file=sys.stderr)
                    poller.unregister(s)
                    s.close()

                    del message_queues[s]

        elif flag & select.POLLHUP:
            print('  closing', client_address, '(HUP)',
                  file=sys.stderr)
            poller.unregister(s)
            s.close()

        elif flag & select.POLLOUT:
            try:
                next_msg = message_queues[s].get_nowait()
            except queue.Empty:
                print(s.getpeername(), 'queue empty',
                      file=sys.stderr)
                poller.modify(s, READ_ONLY)
            else:
                print('  sending {!r} to {}'.format(
                    next_msg, s.getpeername()), file=sys.stderr,
                )
                s.send(next_msg)

        elif flag & select.POLLERR:
            print('  exception on', s.getpeername(),
                  file=sys.stderr)
            poller.unregister(s)
            s.close()

            del message_queues[s]
