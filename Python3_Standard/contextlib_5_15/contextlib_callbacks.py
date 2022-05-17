import contextlib


def callback(*args, **kwargs):
    print('callback {} {}'.format(args, kwargs))


with contextlib.ExitStack() as stack:
    stack.callback(callback, 'a', 'b')
    stack.callback(callback, a='bb')

print('=' * 88)
try:
    with contextlib.ExitStack() as stack:
        stack.callback(callback, 'a', 'b')
        stack.callback(callback, a='bb')
        raise RuntimeError('11111error')
except RuntimeError as e:
    print('Error {}'.format(e))

print('=' * 88)
with contextlib.ExitStack() as stack:
    @stack.callback
    def inline():
        print('inline')
        print('local_resource={!r}'.format(local_resource))


    local_resource = '不昧因果，不落因果'
    print('the context')
