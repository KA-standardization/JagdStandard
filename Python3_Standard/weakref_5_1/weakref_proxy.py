import weakref


class TestObj:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('deleting {}'.format(self))


obj = TestObj('AFFE')

r = weakref.ref(obj)
p = weakref.proxy(obj)

print(obj.name)
print(r().name)
print(p.name)
del obj
print(p.name)
