import contextlib


class Door:

    def __init__(self):
        print('__init__()')
        self.status = 'open'

    def close(self):
        print('  close()')
        self.status = 'close'


with contextlib.closing(Door()) as door:
    print('aaa')

print('='*88)

try:
    with contextlib.closing(Door()) as door:
        raise RuntimeError('runtimeerror')
except Exception as e:
    print('error', e)
