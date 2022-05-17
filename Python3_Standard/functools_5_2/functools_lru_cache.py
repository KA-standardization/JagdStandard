import functools


@functools.lru_cache()
def expensive(a, b):
    print('expensive {} {}'.format(a, b))
    return a + b


MAX = 2

print('First set of calls')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)

print(expensive.cache_info())

print('Second set of calls')
for i in range(MAX + 1):
    for j in range(MAX + 1):
        expensive(i, j)
print(expensive.cache_info())

print('Clearing cache')
expensive.cache_clear()
print(expensive.cache_info())

print('Third set of calls:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())


