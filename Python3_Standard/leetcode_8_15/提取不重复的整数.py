import collections


def foo():
    a = list(input())
    a.reverse()
    res_ = dict()
    r = collections.deque()
    for item in a:
        flag = res_.get(item)
        if flag is None:
            res_[item] = item
            r.append(item)
    print(r)
    s = ""
    for i in r:
        s += i

    return int(s)


print(foo())
# 2752771 1725
# a = 987354
# b = 1000000
# d = 999999
# # 12646
# c = b - a
