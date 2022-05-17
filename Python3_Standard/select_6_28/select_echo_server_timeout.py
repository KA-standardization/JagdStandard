import sys
import select
import socket
import queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address),
      file=sys.stderr)
server.bind(server_address)

server.listen(5)

inputs = [server]

outputs = []

message_queues = {}

while inputs:
    print('waiting for the next event',
          file=sys.stderr)
    timeout = 1
    readable, writable, exceptional = select.select(inputs,
                                                    outputs,
                                                    inputs,
                                                    timeout)

    if not (readable or writable or exceptional):
        print('  timed out, do some other work here',
              file=sys.stderr)
        continue

    for s in readable:

        if s is server:
            connection, client_address = s.accept()
            print('  connection from', client_address,
                  file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            message_queues[connection] = queue.Queue()

        else:
            data = s.recv(1024)
            if data:
                print('  received {!r} from {}'.format(
                    data, s.getpeername()), file=sys.stderr,
                )
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)

            else:
                print('closing', client_address, file=sys.stderr)
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                del message_queues[s]

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            print(s.getpeername(), 'queue empty',
                  file=sys.stderr)
            outputs.remove(s)
        else:
            print('  sending {!r} to {}'.format(
                next_msg, s.getpeername()), file=sys.stderr,
            )
            s.send(next_msg)

    for s in exceptional:
        print('  exception condition on', s.getpeername(),
              file=sys.stderr)
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        del message_queues[s]
