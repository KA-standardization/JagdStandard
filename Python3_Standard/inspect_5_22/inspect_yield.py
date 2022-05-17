import inspect


def foo():
    yield 1
    yield 2


print(inspect.isgeneratorfunction(foo))
gen = foo()
if inspect.getgeneratorstate(gen) == 'GEN_CREATED':
    print('Kaiser')
print(inspect.getgeneratorstate(gen))
print(next(gen))
print(inspect.getgeneratorstate(gen))
print(next(gen))
print(inspect.getgeneratorstate(gen))
