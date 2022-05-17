import operator


class FObj:

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'Fobj--{}'.format(self.arg)


l = [FObj(i) for i in range(5)]
print('l   ', l)

g = operator.attrgetter('arg')
values = [g(i) for i in l]
print('arg   ', values)

l.reverse()
print('r   ', l)
print('s    ', sorted(l, key=g))

print('=' * 88)

l2 = [dict(val=-1 * i) for i in range(4)]
print(l2)
g2 = operator.itemgetter('val')
vals = [g2(i) for i in l2]
print(vals)
print('=' * 88)
l3 = [(i, i * 2) for i in range(4)]
print(l3)
g = operator.itemgetter(1)
vals = [g(i) for i in l3]
print(vals)
