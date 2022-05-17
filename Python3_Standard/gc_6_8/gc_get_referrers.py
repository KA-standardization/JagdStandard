import gc
import pprint


class Graph:

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        print('Linking nodes {}.next = {}'.format(self, next))
        self.next = next

    def __repr__(self):
        return '{} ({})'.format(self.__class__.__name__, self.name)

    def __del__(self):
        print('{}.__del__'.format(self))


one = Graph('one')
two = Graph('two')
three = Graph('three')
one.set_next(two)
two.set_next(three)
three.set_next(one)

print('Collecting')
n = gc.garbage
print('Unreachable objects: {}'.format(n))
pprint.pprint(gc.garbage)

REFERRERS_TO_IGNORE = [locals(), globals(), gc.garbage]
print(REFERRERS_TO_IGNORE)


def find_referring_garbage(obj):
    print('Looking for references to {!r}'.format(obj))
    referrers = (r for r in gc.get_referrers(obj) if r not in REFERRERS_TO_IGNORE)

    for ref in referrers:
        if isinstance(ref, Graph):
            yield ref
        elif isinstance(ref, dict):
            for parent in find_referring_garbage(ref):
                yield parent


print()
print('Clearing referrers')
for obj in [one, two, three]:
    for ref in find_referring_garbage(obj):
        print('Find referrer:', ref)
        ref.set_next(None)
        del ref
    del obj

print()
print('Clearing garbage')
del gc.garbage[:]
print()
print('Collecting')
n = gc.collect()
print('Unreachable objects:', n)
print('Remaining Garbage:', end=' ')
pprint.pprint(gc.garbage)
