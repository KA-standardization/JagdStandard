import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

# 向量化: 利用数组表达式来替代显示循环的方法
points_a = np.array([1, 2, 3, 7])
points_b = np.array([4, 5, 6, 8, 9])

xs, ys = np.meshgrid(points_a, points_b)
pprint(xs)
print()
pprint(ys)

z = np.sqrt(xs + ys)
pprint(z)
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.show()

#########################################################################################################
print('*' * 88)

x = [1, 2, 3, 4, 5, 6, 7]
y = [11, 22, 33, 44, 55, 66, 77]
cond = [True, False, False, True, False, False, True]

res = [x if z else y for x, y, z in zip(x, y, cond)]
print(res)

pprint(np.where(cond, x, y))

# np.where 根据一个数组来生成一个新数组
arr = np.random.randn(4, 4)
pprint(arr)
cond = arr > 0
pprint(cond)
pprint(np.where(cond, 100, 0))

# np.where 将标量和数组联合使用
pprint(np.where(cond, 2, arr))
pprint(np.where(~cond, 2, arr))

#########################################################################################################
print('*' * 88)
# 聚合函数: 缩减函数 既可以调用聚合函数,也可以使用顶层的numpy
arr = np.random.randn(5, 5)
pprint(arr)
pprint(arr.mean())
pprint(np.mean(arr))
# 1表示计算每一列的值 0表示计算行轴向
pprint(arr.sum(axis=1))

#########################################################################################################
print('*' * 88)
# 累加cumsum 累乘cumprod
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pprint(arr.cumsum(dtype=np.int16))
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
pprint(arr.cumsum(axis=0))
pprint(arr.cumprod(axis=1))
# 标准差
pprint(arr.std(axis=0))
# 方差
pprint(arr.var(axis=1))
pprint(arr.min())
pprint(arr.max())
# 最大值位置
pprint(arr.argmax())
# 最小值位置
pprint(arr.argmin())

#########################################################################################################
print('*' * 88)
# 布尔数组

arr = np.random.randn(100)
pprint(arr)
cond = arr > 0
pprint(cond)
# 计算TRUE的个数 True 1 False 0
pprint(cond.sum())
# 至少有一个 True
print(cond.any())
# 所有都是 True
print(cond.all())

#########################################################################################################
print('*' * 88)
# 数组的按位排序  np.sort数组的拷贝
arr = np.random.randn(6)
pprint(arr)
arr.sort()
pprint(arr)

arr = np.random.randn(5, 3)
pprint(arr)
pprint(np.sort(arr, axis=0))
pprint(arr)

#########################################################################################################
print('*' * 88)
# 分为数 百分之5的数
arr = np.random.randn(100)
arr.sort()
pprint(arr[int(0.05 * len(arr))])

#########################################################################################################
print('*' * 88)
# np.unique 返回数组中唯一值排序后形成的数组
names = np.array(['a', 'c', 'c', 'b', 'a', 'd'])
pprint(np.unique(names))
# 检查一个数组中的值是否在另一个数组中
arr = np.array([6, 9, 8, 8, 0, 4, 2])
cond = np.in1d(arr, [7, 9, 4])
pprint(cond)
pprint(arr[cond])

x = np.array([6, 9, 8, 8, 0, 4, 2])
y = np.array([16, 9, 18, 8, 10, 4, 12])
# x y 交集 并排序
print('交集: ', end='')
pprint(np.intersect1d(x, y))
# x y 并集
print('并集: ', end='')
pprint(np.union1d(x, y))
# x y 差集 在x 中 不在y中
print('差集: ', end='')
pprint(np.setdiff1d(x, y))
# 异或集 在x中或y中,但不属于x,y交集的元素
print('异或集: ', end='')
pprint(np.setxor1d(x, y))
