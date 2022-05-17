import functools
import itertools
import operator
import pprint


@functools.total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)


data = list(map(Point, itertools.cycle(itertools.islice(itertools.count(), 3)), itertools.islice(itertools.count(), 7)))
pprint.pprint(data, width=35)
print('=' * 88)

for k, g in itertools.groupby(data, operator.attrgetter('y')):
# for k, g in itertools.groupby(data):
    print(k, list(g))
