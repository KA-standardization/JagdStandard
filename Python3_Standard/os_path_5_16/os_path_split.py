import os.path

PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
]

for path in PATHS:
    print('{!r:>17} : {}'.format(path, os.path.split(path)))
    # 第一部分
    print('{!r:>25} : {}'.format(path, os.path.dirname(path)))
    # 第二部分
    print('{!r:>50} : {}'.format(path, os.path.basename(path)))

print('=' * 88)
PATHS2 = [
    'filename.txt',
    'filename',
    '/path/to/filename.txt',
    '/',
    '',
    'my-archive.tar.gz',
    'no-extensin.',
]

for path in PATHS2:
    print('{!r:>21} : {!r}'.format(path, os.path.splitext(path)))

print('=' * 88)
PATHS3 = [
    'one/two/three/foo',
    'one/two/threedd',
    'one/two/three/fa',
    'one/two/three/cc',
]

print(os.path.commonprefix(PATHS3))
print(os.path.commonpath(PATHS3))

p = r'C:\Users\root\AppData\Roaming\aaa.txt'
_, filename = os.path.split(p)
print(filename)
