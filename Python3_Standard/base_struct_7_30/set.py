# 创建一个空集合必须用 set() set无序且不重复元素序列
# 类似列表推导式，同样集合支持集合推导式(Set comprehension):
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
'''
add()	    为集合添加元素
update()	给集合添加元素

discard()	删除集合中指定的元素
remove()	移除指定元素
pop()	    随机移除元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合

isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。

union()	返回两个集合的并集
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。

issubset()	    判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
'''
