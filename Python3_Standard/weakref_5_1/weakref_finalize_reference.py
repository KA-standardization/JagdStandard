import gc
import weakref


class TestObj:
    c = 2

    def __del__(self):
        print('delete {}'.format(self))


def on_finalize(*args):
    print('args {!r}'.format(args))


obj = TestObj()
obj_id = id(obj)
print(obj_id)
f = weakref.finalize(obj, on_finalize, obj)
f.atexit = False

del obj

for ele in gc.get_objects():
    if id(ele) == obj_id:
        print('ele {}'.format(ele))
        print(id(ele))

