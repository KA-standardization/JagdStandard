import sys
import codecs
import socket
import threading
import socketserver


class Echo(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        self.request.send(data)
        return


if __name__ == '__main__':
    address = ('localhost', 0)
    server = socketserver.TCPServer(address, Echo)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    text = 'Jäger'
    # len_sent = s.send(text)
    len_sent = s.send(text.encode())

    response = s.recv(len_sent)
    print(repr(response))

    s.close()
    server.socket.close()
