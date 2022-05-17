import contextlib


class NonFatalError(Exception):
    pass


def non_operation():
    raise NonFatalError('The operation')


try:
    print('try operation')
    non_operation()
    print('sucess')
except NonFatalError:
    pass

print('done')

print('=' * 88)

with contextlib.suppress(NonFatalError):
    print('try2 ')
    non_operation()
    print('sucess2')
