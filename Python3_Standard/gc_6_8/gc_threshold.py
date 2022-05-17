import gc
import sys
import pprint

print(gc.get_threshold())

try:
    threshold = int(sys.argv[1])
except (IndexError, ValueError, TypeError) as err:
    print(err)
    threshold = 5


class Foo:

    def __init__(self, name):
        self.name = name
        print('Create', self.name)


gc.set_debug(gc.DEBUG_STATS)

args = (threshold, 1, 1)
gc.set_threshold(*args)
print(gc.get_threshold())
gc.collect()
print()

print('Creating objects')
objs = []
for i in range(10):
    objs.append(Foo(i))
print('Exiting')

# turn off debugging
gc.set_debug(0)
