import contextlib


class Context(contextlib.ContextDecorator):

    def __init__(self, message):
        self.message = message
        print('__init__ {}'.format(message))

    def __enter__(self):
        print('__enter__ {}'.format(self.message))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ {}'.format(self.message))


@Context('aaa')
def foo(message):
    print(message)


print('=' * 88)

with Context('bbb'):
    print('Context')

print('='*88)
foo('ccc')
