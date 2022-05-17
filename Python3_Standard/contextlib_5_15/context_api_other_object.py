class WithContext:

    def __init__(self, context):
        print('WithContext.__init__ {}'.format(context))

    def foo(self):
        print('WithContext')

    def __del__(self):
        print('WithContext del')


class Context:

    def __init__(self):
        print('Context__init__')

    def __enter__(self):
        print('enter __enter__')
        return WithContext(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context __exit__')

# c关联__enter__返回的对象
with Context() as c:
    c.foo()
