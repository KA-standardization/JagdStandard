import contextlib


@contextlib.contextmanager
def foo():
    print('  entering')
    try:
        yield
    except RuntimeError as e:
        print('ERROR', e)
    finally:
        print('  exiting')


@foo()
def normal():
    print('  normal')


@foo()
def throw_error(err):
    raise err


normal()
print('==')
throw_error(RuntimeError('runtimeerror'))
print('==')
throw_error(ValueError('valueerror'))


