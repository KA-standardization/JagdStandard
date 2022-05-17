import operator

a = -1
b = 5.0
c = 2
d = 6

print(operator.abs(a))
print(operator.neg(a))
print(operator.neg(b))
print(operator.pos(a))
print(operator.pos(b))
print('=' * 88)
print(operator.add(a, b))
print(operator.floordiv(a, b))
print(operator.truediv(a, b))
print(operator.mod(a, b))
print(operator.mul(a, b))
print(operator.pow(c, d))
print(operator.sub(b, a))
print('=' * 88)
print(operator.and_(c, d))
print(operator.invert(c))
print(operator.lshift(c, d))
print(operator.rshift(d, c))
print(operator.or_(c, d))
print(operator.xor(c, d))
