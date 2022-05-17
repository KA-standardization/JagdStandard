import contextlib


@contextlib.contextmanager
def make_context(i):
    print('{} enter'.format(i))
    yield
    print('{} exiting'.format(i))


def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        # for i in range(n):
        stack.enter_context(make_context('1'))
        print(msg)


variable_stack(2, 'hell')
