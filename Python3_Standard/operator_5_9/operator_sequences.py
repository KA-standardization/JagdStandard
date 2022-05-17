import operator

a = [1, 2, 3]
b = ['a', 'b', 'c']

print(operator.concat(a, b))
print(operator.contains(a, 4))
print(operator.countOf(a, 3))
print(operator.indexOf(a, 1))
print('=' * 88)
print(operator.getitem(b, 2))
print(operator.getitem(b, slice(1, 3)))
operator.setitem(b, 1, 'A')
print(b)
operator.delitem(a, 1)
print(a)
