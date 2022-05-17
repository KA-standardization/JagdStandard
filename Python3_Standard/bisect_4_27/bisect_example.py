import bisect

data = [14, 85, 11, 34, 20, 16, 77, 888, 945, 34, 234, 567]
l = []
for i in data:
    position = bisect.bisect(l, i)
    # bisect.insort(l, i)
    # bisect.insort_right(l, i)
    bisect.insort_left(l, i)
    print('{:3} {:3}'.format(i, position), l)

print(sorted(data))
print(bisect.bisect(sorted(data), 16))
