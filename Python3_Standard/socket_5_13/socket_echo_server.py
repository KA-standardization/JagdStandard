import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('{} {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            date = connection.recv(16)
            print('received {!r}'.format(date))
            if date:
                connection.sendall(date)
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()
