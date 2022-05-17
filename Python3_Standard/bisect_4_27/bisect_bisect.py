import bisect

"""
bisect( haystack, needle) 在 haystack（ 干草垛） 里搜索 needle（ 针） 的位置， 该位置满足的条件是， 把 needle 插入这个位置之后， 
haystack 还能保持升序。 也就是在说这个函数返回的位置前面的值， 都小于或等于 needle 的值。 其中 haystack 必须是一个有序的序列。 
你可以先用 bisect( haystack, needle) 查找位置 index， 再用 haystack.insert( index, needle) 来插入新值。 
但你也可用 insort 来一步到位， 并且后者的速度更快一些。
"""


def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    i = bisect.bisect(breakpoints, score)
    print(i)
    return grades[i]


l = [grade(s) for s in [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]]
print(l)
