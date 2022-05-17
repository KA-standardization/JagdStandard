from pprint import pprint

import numpy as np

# 数组跨度: 具有跨步信息,使数组能够以不同的步长在内存中移动
'''
    指向数据的指针,即RAM中或内存映射文件中的数据块
    数据类型或dtype,描述数组中固定大小的值单元格
    表示数组的形状(shape)的元组
    步长元组,表示要步进的字节数的整数以便沿维度推进一个元素
'''

arr = np.ones((3, 5))
pprint(arr)
# 跨度
print(arr.strides)

#########################################################################################################
print('*' * 88)
ints = np.ones(10, dtype=np.uint16)
floats = np.ones(10, dtype=np.float32)
print(np.issubdtype(ints.dtype, np.integer))
print(np.issubdtype(floats.dtype, np.floating))
# 查看所有父类
pprint(np.float64.mro())

arr = np.arange(8)
# 行方向重塑
pprint(arr.reshape((2, 4), order='C'))
# 列方向重塑
pprint(arr.reshape((2, 4), order='F'))
# -1 维度数据可以通过数据进行推断
pprint(arr.reshape((2, -1)))

#########################################################################################################
print('*' * 88)
# 扁平化 flattening 分散化 raveling
arr = np.arange(15).reshape((5, -1))
pprint(arr)
# 不会生成底层数值的副本
pprint(arr.ravel())
# 返回数据的副本
pprint(arr.flatten())

#########################################################################################################
print('*' * 88)
# 行 C顺序
# 列 Fortran顺序

arr = np.arange(15).reshape((3, 5))
pprint(arr)
# C
pprint(arr.ravel())
# F
pprint(arr.ravel('F'))

#########################################################################################################
print('*' * 88)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

# 行链接 按行堆叠数组
pprint(np.concatenate([arr1, arr2], axis=0))
# 延着0轴
pprint(np.vstack((arr1, arr2)))
pprint(np.row_stack((arr1, arr2)))
# 列链接 按列堆叠数组
pprint(np.concatenate([arr1, arr2], axis=1))
# 延着1轴
pprint(np.hstack((arr1, arr2)))
pprint(np.column_stack((arr1, arr2)))

#########################################################################################################
print('*' * 88)
# split 将一个数组延轴向切片成多个数组

arr = np.arange(15).reshape((5, -1))
pprint(arr)
# [1,3]表示将数组拆分时索引的位置
x, y, z = np.split(arr, [1, 3])
pprint(x)
pprint(y)
pprint(z)
arr = np.arange(12).reshape((3, -1))
print('np.hsplit 0轴')
pprint(np.hsplit(arr, 2))
print('np.vsplit 1轴')
pprint(np.vsplit(arr.reshape((4, -1)), 2))

print('dstack 2轴')
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
pprint(arr)
print(arr.shape)
pprint(np.dstack((arr)))
#########################################################################################################
print('*' * 88)

arr = np.arange(6).reshape((3, -1))
arr2 = np.random.randn(3, 2)
# 按行堆叠
pprint(np.r_[arr, arr2])

# 按列堆叠
pprint(np.c_[arr, arr2])

# 将切片转换为数组
pprint(np.c_[1:6, -10:-5])

#########################################################################################################
print('*' * 88)
# 复制数组

arr = np.arange(3)
pprint(arr)
pprint(arr.repeat(3))
# [2,3,4] 复制不同的次数
pprint(arr.repeat([2, 3, 4]))
# 多维数组可以在指定的轴向上对它们的元素进行复制
# 如果没有传递轴,数组首先扁平化

arr2 = np.random.randn(2, 2)
pprint(arr2)

pprint(arr2.repeat([2, 3], axis=0))
pprint(arr2.repeat([2, 3], axis=1))
# tile 逐行进行的

pprint(np.tile(arr2, 2))
pprint(np.tile(arr2, (2, 1)))

#########################################################################################################
print('*' * 88)

arr = np.arange(10) * 100
pprint(arr)

# 根据索引替换 指定元素
pprint(arr.take([7, 2, 3, 1]))
arr.put([7, 2, 3, 1], 99)
pprint(arr)
arr.put([7, 2, 3, 1], [11, 22, 33, 44])
pprint(arr)

arr = np.random.randn(2, 4)
pprint(arr)
# 重复两边 轴2
pprint(arr.take([2, 0, 2, 1], axis=1))

#########################################################################################################
print('*' * 88)
# 广播 标量值与数组组合的时候

arr = np.random.randn(4, 3)
pprint(arr)

pprint(arr.mean(axis=0))
pprint(arr - arr.mean(0))
#########################################################################################################
print('*' * 88)
# 多维度
arr = np.random.randn(2, 3, 4)
pprint(arr)

# 0轴
pprint(arr - np.ones((3, 1)))
# 1轴
pprint(arr - np.ones((1, 4)))

arr = np.ones((4, 4))
pprint(arr)
# np.newaxis 增加一个维度
arr_3 = arr[:, np.newaxis, :]
pprint(arr_3)
# 4 1 4
print(arr_3.shape)
# 三维数组在轴2上减去均值,

arr = np.random.randn(3, 4, 5)
pprint(arr)
pprint(arr.mean(axis=2))
# 3 4 5
#   3 4
# pprint(arr - arr.mean(2)[:, :])
# 3 4 5
# 3 4 1
pprint(arr - arr.mean(2)[:, :, np.newaxis])
#########################################################################################################
print('*' * 88)


# [:, :, np.newaxis]推广到N维
# 在一个轴向上减去均值又不牺牲性能的方法

def demean_axix(arr, axis=0):
    means = arr.mean(axis)
    indexer = [slice(None)] * arr.ndim
    indexer[axis] = np.newaxis
    return arr - means[indexer]


#########################################################################################################
print('*' * 88)
# 广播设定数组的值
arr = np.zeros((4, 3))
pprint(arr)
arr[:] = 5
pprint(arr)
col = np.array([111, 222, 333, 444])

arr[:] = col[:, np.newaxis]
pprint(arr)
#########################################################################################################
print('*' * 88)
# add.reduce
arr = np.arange(10)
print(np.add.reduce(arr))
# np.all()
np.random.seed(1024)
arr = np.random.randn(5, 5)
arr[::2].sort(1)
cond = arr[:, :-1] < arr[:, 1:]
pprint(arr)
pprint(arr[:, :-1])
pprint(arr[:, 1:])
pprint(np.logical_and.reduce(cond, axis=1))
# outer形成交叉乘积 输出维度等于输入维度总和
arr = np.arange(3).repeat([2, 2, 2])
pprint(arr)
pprint(np.multiply.outer(arr, np.arange(6)))

x, y = np.random.randn(3, 4), np.random.randn(5)
res = np.subtract.outer(x, y)
pprint(res)
pprint(res.shape)
#########################################################################################################
print('*' * 88)
# 简介排序
arr = np.array([5, 0, 1, 3, 2])
# quicksort mergesort heapsort
# n^2       n log n   n log n
index = arr.argsort(kind='mergesort')
pprint(index)
pprint(arr[index])
arr = np.random.randn(3, 5)
arr[0] = np.array([5, 0, 1, 3, 2])
pprint(arr)
pprint(arr[:, arr[0].argsort()])
# lexsort: 对多建数组进行间接字典排序
# 排序的键的顺序从传递的最后一个数组开始
first_name = np.array(['bbb', 'jjj', 'sss', 'bii', 'bar'])
last_name = np.array(['jbb', 'jjj', 'ass', 'bii', 'car'])
sotter = np.lexsort((first_name, last_name))
pprint(sotter)
pprint(first_name[sotter])

#########################################################################################################
print('*' * 88)
arr = np.random.randn(20)
pprint(arr)
# 前三个最小 没有特定顺序
print(np.partition(arr, 3))
# np.argpartition 返回将数组重新排序的索引
index = np.argpartition(arr, 3)
pprint(index)
#########################################################################################################
print('*' * 88)
# searchsorted 在已排序的数组寻找元素
arr = np.array([1, 2, 4, 55, 666, 777])
# side='right' 一组等值右侧的索引
pprint(arr.searchsorted(2, side='right'))
#########################################################################################################
print('*' * 88)
# 桶边界
data = np.ceil(np.random.uniform(0, 10000, 50))
pprint(data)
bins = np.array([0, 100, 1000, 5000, 10000])
labels = bins.searchsorted(data)
pprint(labels)
#########################################################################################################
print('*' * 88)
# np.memmap: 允许将大型文件以小堆栈的方式进行读取和写入,而无需将整个数组载入内存
# 传入文件路径, dtype mode shape 必须指定dtype shape 因为该文件只是磁盘上没有元数据的二进制数据块
# mmap = np.memmap('mmap', dtype='int64', mode='w+', shape=(10000, 10000))
# + 读写接可
mmap = np.memmap('mmap', dtype='int64', mode='r+', shape=(10000, 10000))
# 对mmap的切片返回的是硬盘上的数据视图
arr = mmap[:5]
pprint(arr)
pprint(arr.flags)
# 将数据赋值给这些切片,它将会在内存中缓冲
arr[:] = np.ones((5, 10000))
pprint(arr)
mmap.flush()
pprint(mmap[:1])
for ele in mmap[:1]:
    print(ele)

#########################################################################################################
print('*' * 88)
arr2 = np.arange(6).reshape((2, -1))
pprint(arr2)
print(arr2.flags)
arr2.copy('F').flags
print(arr2.flags)
