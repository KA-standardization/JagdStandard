import gc
import pprint
import queue


class Graph:

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        print('Linking nodes {}.next= {}'.format(self, next))
        self.next = next

    def __repr__(self):
        return '{} ({})'.format(self.__class__.__name__, self.name)


one = Graph('one')
two = Graph('two')
three = Graph('three')
one.set_next(two)
two.set_next(three)
three.set_next(one)

for ref in gc.get_referents(three):
    pprint.pprint(ref)

print('=' * 88)
seen = set()
to_process = queue.Queue()
to_process.put(([], three))

while not to_process.empty():
    chain, next = to_process.get()
    chain = chain[:]
    chain.append(next)
    print('Examining:', repr(next))
    seen.add(id(next))
    for r in gc.get_referents(next):
        if isinstance(r, str) or isinstance(r, type):
            # print('isinstance {}'.format(r))
            pass
        elif id(r) in seen:
            print()
            print('Found a cycle to {}'.format(r))
            for i, link in enumerate(chain):
                print('   {}'.format(i), end=' ')
                pprint.pprint(link)
        else:
            # print('chain {}'.format(chain))
            to_process.put((chain, r))

print(seen)
print(one.__dict__)
print(two.__dict__)
print(three.__dict__)
