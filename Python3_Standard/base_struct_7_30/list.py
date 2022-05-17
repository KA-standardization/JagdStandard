# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
'''  list包含以下函数
len(list)   列表元素个数
max(list)   返回列表元素最大值
min(list)   返回列表元素最小值
list(seq)   将元组转换为列表
'''
""" list 包含以下方法
list.copy()                 复制列表
list.append(obj)            在列表末尾添加新的对象
list.extend(seq)            在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.insert(index, obj)     将对象插入列表

list.remove(obj)            移除列表中某个值的第一个匹配项
list.pop([index=-1])        移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.clear()                清空列表

list.index(obj)             从列表中找出某个值第一个匹配项的索引位置
list.count(obj)             统计某个元素在列表中出现的次数
list.reverse()              反向列表中元素
list.sort( key=None, reverse=False)     对原列表进行排序
"""
"""
l2 = list(l1)
l2 = l1[:]
构造方法或[:]做的是浅复制（ 即复制了最外层容器，副本中的元素是源容器中元素的引用）。
如果所有元素都是不可变的，那么这样没有问题，还能节省内存。但是，如果有可变的元素，可能就会导致意想不到的问题。
"""