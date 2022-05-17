import socket
from urllib.parse import urlparse

URLS = [
    'http://www.python.org',
    'https://www.mybank.com',
    'ftp://prep.ai.mit.edu',
    'gopher://gopher.xxx.edu',
    'smtp://mail.example.com',
    'imap://mail.example.com',
    'imaps://mail.example.com',
    'pop3://pop.example.com',
    'pop3s://pop.example.com',
]

for url in URLS:
    parsed_url = urlparse(url)
    port = socket.getservbyname(parsed_url.scheme)
    print(parsed_url.scheme, port)

print('=' * 88)

for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
    url = '{}://example.com'.format(socket.getservbyport(port))
    print(url)

print('=' * 88)


def get_constants(prefix):
    return {getattr(socket, n): n
            for n in dir(socket) if n.startswith(prefix)}


protocols = get_constants('IPPROTO_')
print(protocols)
for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print('{} --> {} (socket.{}={})'.format(name, proto_num, const_name, getattr(socket, const_name)))

print('=' * 88)
families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')
print(families)
print(types)
print(protocols)

for response in socket.getaddrinfo('www.python.org', 'http'):
    print(response)
    family, socktype, proto, canonname, sockaddr = response
    print(families[family])
    print(types[socktype])
    print(protocols[proto])
    print(canonname)
    print(sockaddr)
    print()

print('=' * 88)
responses = socket.getaddrinfo(host='www.baidu.com', port='http', family=socket.AF_INET, type=socket.SOCK_STREAM,
                               proto=socket.IPPROTO_TCP, flags=socket.AI_CANONNAME)
for response in responses:
    print(response)
