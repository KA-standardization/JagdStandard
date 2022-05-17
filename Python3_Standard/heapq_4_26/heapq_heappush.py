import heapq
import itertools
import random

from heapq_showtree import show_tree

data = [19, 9, 4, 11, 16]
heap = []
print(data)
for n in data:
    print('add {:>3}'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)

print('=' * 50)
heapq.heapify(data)
show_tree(data)

print('=' * 50)
for i in range(2):
    smallest = heapq.heappop(data)
    print('{:>3}'.format(smallest))
    show_tree(data)

print('=' * 50)
for n in [0, 13]:
    heapq.heapreplace(data, n)
    show_tree(data)

# sorted(data)[-2:]
# sorted(data)[:2]
print(heapq.nlargest(2, data))
print(heapq.nsmallest(2, data))

data2 = [119, 91, 41, 111, 171]
print(list(itertools.chain(data2, data)))

data3 = []
for i in range(4):
    new_data = list(random.sample(range(1, 101), 5))
    new_data.sort()
    data3.append(new_data)

print(data3)
for i, d in enumerate(data3):
    print('{} {}'.format(i, d))

for i in heapq.merge(*data3):
    print(i, end=' ')
