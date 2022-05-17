import weakref


class TestObj:
    def __del__(self):
        print('delete {}'.format(self))


def on_finalize(*args):
    print('on_finalize{!r}'.format(args))


obj = TestObj()
r = weakref.finalize(obj, on_finalize, 'aber')
r.atexit = False

del obj
