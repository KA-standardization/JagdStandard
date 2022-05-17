import weakref


class TestObj:
    def __del__(self):
        print('test deleting {}'.format(self))


obj = TestObj()
r = weakref.ref(obj)
print(obj)
print(r)
print(r())
del obj
print(r())

print('=' * 88)

obj2 = TestObj()


def callback(reference):
    print('callback {!r}'.format(reference))


r2 = weakref.ref(obj2, callback)
print(obj2)
print(r2)
print(r2())
del obj2
print(r())
