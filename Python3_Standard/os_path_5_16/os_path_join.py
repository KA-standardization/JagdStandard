import os
import time
import os.path

PATHS = [
    ('one', 'two', 'three'),
    ('/one', '/two', '/three'),
    ('/', 'one', 'two', 'three'),
]

for path in PATHS:
    print(os.path.join(*path))

print('=' * 88)
for user in ['', 'dh', 'nos']:
    lookup = '~' + user
    print(os.path.expanduser(lookup))

print('=' * 88)
os.environ['FISHER'] = 'e'
print(os.path.expandvars('/l/o/v/$FISHER'))

print('=' * 88)
PATHS = [
    'one//two//three',
    'one/./two/./three',
    'one/../alt/aa/bb'
]
for path in PATHS:
    print(os.path.normpath(path))

print('=' * 88)
os.chdir('/python_code')

PATHS = [
    '.',
    '..',
    './one/two/three',
    '../one/two/three'
]

for path in PATHS:
    print(os.path.abspath(path))

print('=' * 88)
print(__file__)
# 访问
print(time.ctime(os.path.getatime(__file__)))
# 修改
print(time.ctime(os.path.getmtime(__file__)))
# 创建
print(time.ctime(os.path.getctime(__file__)))
print(os.path.getsize(__file__))
print(os.stat(__file__))
print(time.ctime(os.stat(__file__).st_ctime))

print('=' * 88)

FILENAMES = [
    __file__,
    os.path.dirname(__file__),
    '/',
    './broken_link',
]
for file in FILENAMES:
    print(file)
    print(os.path.isabs(file))
    print(os.path.isfile(file))
    print(os.path.isdir(file))
    print(os.path.islink(file))
    print(os.path.ismount(file))
    print(os.path.exists(file))
    print(os.path.lexists(file))
    print()
