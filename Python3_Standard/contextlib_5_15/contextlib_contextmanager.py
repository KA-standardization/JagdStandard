import contextlib


@contextlib.contextmanager
def make_context():
    print('  entering')
    try:
        yield {}
    except RuntimeError as e:
        print('ERROR', e)
    finally:
        print('  exiting')


print('Normal')
with make_context() as m:
    print('  inside',m)

print('\nHandled error')
with make_context() as m:
    raise RuntimeError('example handled error')

print('\nUnhandled error')
with make_context() as m:
    raise ValueError('example no handled error')