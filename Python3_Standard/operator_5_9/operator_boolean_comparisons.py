import operator

a = 1
b = 5
print(operator.not_(a))
print(operator.truth(a))
print(operator.is_(a, b))
print(operator.is_not(a, b))

print('=' * 88)
for func in (operator.lt, operator.le, operator.eq, operator.ne, operator.ge, operator.gt):
    print('{}(a, b): {}'.format(func.__name__, func(a, b)))
