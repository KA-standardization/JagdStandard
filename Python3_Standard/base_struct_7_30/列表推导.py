"""
列表推导是构建列表（ list） 的快捷方式， 而生成器表达式则可以用来创建其他任何类型的序列。
"""
# 列表推导笛卡尔积
colors = ['RED', 'BLK']
sizes = ['S', 'M', 'L']
t = [(c, z) for c in colors for z in sizes]
print(t)
for t in ('%s - %s' % (c, z) for c in colors for z in sizes):
    print(t)
########################################################################################################################
a, b, *c = range(5)
print(c)
