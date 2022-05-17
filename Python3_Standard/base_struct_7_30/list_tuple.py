l = ['a', 'b', 'c', 'd']
l2 = [1, 2, 3, 4]
l3 = [1, 2, 3, 4]
l4 = [1, 2, 3, 4]
t = ('q', 'w', 'e', 'r')
t2 = (5, 6, 7, 8)

# s + s2， 拼接
print(l.__add__(l2))
print(t.__add__(t2))
"""
如果一个函数或者方法对象进行的是就地改动,那它就应该返回None
"""
# s + = s2， 就地拼接
print(l.__iadd__(l2))
print()
# 在尾部添加一个新元素
print(l3.append('A'), l3)
print()
# 删除所有元素
print(l3.clear(), l3)
print()
# s 是否包含 e
print(l.__contains__('b'))
print(t.__contains__('w'))
# 列表的浅复制
print(l.copy())
print()
# e 在 s 中出现的次数
print(l.count(1))
print(t.count(1))
# 把位于 p 的元素删除
print(l4.__delitem__(0), l4)
print()
# 把可迭代对象 it 追加给 s
print(l4.extend((6, 7, 8, 9)), l4)
print()
# s[ p]， 获取位置 p 的元素
print(l.__getitem__(0))
print(t.__getitem__(0))
# 在 s 中找到元素 e 第一次出现的位置
print(l.index('a'))
print(t.index('q'))
# 在位置 p 之前插入元素 e
print(l4.insert(0, 'B'), l4)
print()
# 获取 s 的迭代器
print(l.__iter__().__next__(), l)
print(t.__iter__().__next__(), t)
# len( s)， 元素的数量
print(l.__len__())
print(t.__len__())
# s * n， n 个 s 的重复拼接
print(l.__mul__(2))
print(t.__mul__(2))
# s *= n， 就地重复拼接
print(l.__imul__(2), l)
print()
# n * s， 反向拼接 *
print(l.__rmul__(2))
print(t.__rmul__(2))
# 删除最后或者是（ 可选的） 位于 p 的元素， 并返回它的值
print(l)
print(l.pop(), l.pop(0), l)
print()
# 删除 s 中的第一次出现的 e
print(l.remove(1), l)
print()
# 就地把 s 的元素倒序排列
print(l.reverse(), l)
print()
# 返回 s 的倒序迭代器
print(l.__reversed__().__iter__().__next__())
print()
# s[ p] = e， 把元素 e 放在位置 p， 替代已经在那个位置的元素
print(l.__setitem__(0, 100), l)
print()
# 就地对 s 中的元素进行排序， 可选的参数有键（ key） 和是否倒序（ reverse）
l5 = [2, 1, 11]
print(l5.sort(), l5)
"""
对元组t来说，t[:]不创建副本，而是返回同一个对象的引用。此外，tuple(t)获得的也是同一个元组的引用。
"""
