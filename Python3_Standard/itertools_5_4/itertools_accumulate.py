import itertools

print(list(itertools.accumulate(range(5))))
print(list(itertools.accumulate('hello')))


def foo(a, b):
    print(a, b)
    return b + a + b


print(list(itertools.accumulate('world', foo)))
