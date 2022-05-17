import socket

print(socket.gethostname())

print('=' * 88)
HOSTS = [
    'baidu.com',
    'www.bilibili.com',
    'pinduoduo.com',
    'www.zhihu.com',
    'pymotw.com'
]
for host in HOSTS:
    try:
        print('{}: {}'.format(host, socket.gethostbyname(host)))
    except socket.error as emsg:
        print('{}: {}'.format(host, emsg))

print('=' * 88)
for host in HOSTS:
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print('HostName {}'.format(name))
        print('Aliases {}'.format(aliases))
        print('Addresses {}'.format(addresses))
    except socket.error as emsg:
        print('Error {}'.format(emsg))
    print()

print('=' * 88)
for host in HOSTS:
    print('{}: {}'.format(host, socket.getfqdn(host)))

print('=' * 88)
hostname, aliases, addresses = socket.gethostbyaddr('66.33.211.242')
print(hostname, aliases, addresses)
