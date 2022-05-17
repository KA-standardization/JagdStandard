# 键必须是唯一的，但值则不变。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，将显示后一个值，
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
''' 字典包含了以下内置函数
len(dict)   计算字典元素个数，即键的总数。
str(dict)   输出字典，以可打印的字符串表示。
type(variable)     返回输入的变量类型，如果变量是字典就返回字典类型。
'''
''' 字典包含了以下内置方法
radiansdict.clear()
删除字典内所有元素
2	radiansdict.copy()
返回一个字典的浅复制
3	radiansdict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值
5	key in dict
如果键在字典dict里返回true，否则返回false
6	radiansdict.items()
以列表返回可遍历的(键, 值) 元组数组
7	radiansdict.keys()
返回一个迭代器，可以使用 list() 来转换为列表
8	radiansdict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2)
把字典dict2的键/值对更新到dict里
10	radiansdict.values()
返回一个迭代器，可以使用 list() 来转换为列表
11	pop(key[,default])
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem()
返回并删除字典中的最后一对键和值。
'''

a = {1: 1, 2: 2, 3: 3, 4: 4}
print(a.popitem())
print(a)
