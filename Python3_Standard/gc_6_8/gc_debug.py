import gc

# flags = (gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_SAVEALL)
flags = gc.DEBUG_LEAK

gc.set_debug(flags)


class Graph:

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        print('Linking nodes {}.next= {}'.format(self, next))
        self.next = next

    def __repr__(self):
        return '{} ({})'.format(self.__class__.__name__, self.name)


class CleanupGraph(Graph):

    def __del__(self):
        print('{}.__del__()'.format(self))


one = Graph('one')
two = Graph('two')
one.set_next(two)
two.set_next(one)

three = CleanupGraph('three')
four = CleanupGraph('four')
five = CleanupGraph('five')
four.set_next(five)
five.set_next(four)

one = two = three = four = five = None

print('Collecting')
gc.collect()
print('Done')

for o in gc.garbage:
    if isinstance(o, Graph):
        print('Retained: {} 0x{:x}'.format(o, id(o)))

gc.set_debug(0)
