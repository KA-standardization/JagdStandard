import numpy as np
from pprint import pprint

data = np.random.randn(2, 3)
pprint(data)
pprint(data + data)
pprint(data * 10)
pprint(data.shape)
pprint(data.ndim)
pprint(data.dtype)

#########################################################################################################
print('*' * 88)
tmp_l = [1, 2, 33, 44, 55]
tmp_l_2 = [1, 2, 3, 7.6, 99, 100]
n_array = np.array(tmp_l)
pprint(n_array)
pprint(n_array.dtype)
n_array_2 = np.array(tmp_l_2, dtype=float)
pprint(n_array_2)
pprint(n_array_2.dtype)

#########################################################################################################
print('*' * 88)
n_zero = np.zeros(10, dtype=np.int16)
pprint(n_zero)
n_zero_2 = np.zeros((2, 3))
pprint(n_zero_2)
n_empty = np.empty((2, 3, 2))
pprint(n_empty)

#########################################################################################################
print('*' * 88)
n_l = [1, 2, 3, 4, 5]
n_a = np.asarray(n_l)
pprint(n_a.dtype)
# asarray 如果输入已经是ndarray则不在复制
n_a_2 = np.asarray(n_zero)
print(id(n_zero))
print(id(n_a_2))

#########################################################################################################
print('*' * 88)
n_o = np.ones(10)
n_o_l = np.ones_like(n_zero)
pprint(n_o)
pprint(n_o_l)
# f_l = np.full()
# f_l_l = np.full_like(n_zero,)
# pprint(f_l)
# pprint(f_l_l)
#########################################################################################################
print('*' * 88)
n_ = np.zeros(10, dtype=np.int32)
print(n_.dtype)
n_2 = n_.astype(np.float32)
print(n_2.dtype)

#########################################################################################################
print('*' * 88)
# 向量化: 任何两个等尺寸数组之间的算术操作都应用了逐元素操作的方法
arr = np.random.randn(2, 3)
pprint(arr)
pprint(arr * arr)
pprint(arr - arr)
# 带有标量的计算算术操作,会把参数传递给数组的每一个元素
# pprint(arr ** 0.5)
pprint(arr ** 2)
# 数组之间的比较会产生一个布尔数组
pprint(arr > (arr * 0.5))

#########################################################################################################
print('*' * 88)
# 数组切片是原数组的视图
arr = np.array([1, 2, 3, 4, 5, 6])
pprint(arr)
arr_slice = arr[2:5]
pprint(arr_slice)
arr_slice[0] = 125
pprint(arr)
arr_slice[:] = 789
pprint(arr)
# 显示复制数组
arr_slice_copy = arr[2:5].copy()
pprint(arr_slice_copy)
pprint(arr)
arr_slice_copy[:] = 5
pprint(arr_slice_copy)
pprint(arr)

#########################################################################################################
print('*' * 88)
# 高维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pprint(arr)
pprint(arr.shape)
pprint(arr[0])
pprint(arr[0][1])

pprint(arr[:1])
pprint(arr[:, :1])
arr = np.random.randn(2, 3, 4)
pprint(arr)
pprint(arr[:, :1, :])

#########################################################################################################
print('*' * 88)
# 布尔数组
names = np.array(['Kaiser', 'Buch', 'holle', 'lebeau', 'ich', 'Kaiserin'])
data = np.random.randn(6, 4)
pprint(data)
pprint(data[names == 'Kaiser'])
pprint(data[names == 'Kaiser', 2:])
pprint(data[~(names == 'Kaiser'), 2:])
pprint(data[(names == 'Kaiser') | (names == 'Kaiserin'), :1])

#########################################################################################################
print('*' * 88)
arr = np.random.randn(2, 3)
pprint(arr)
arr[arr < 0] = 0
pprint(arr)

#########################################################################################################
# 神奇索引:将数据复制到一个新数组中
print('*' * 88)
arr = np.empty((8, 4))
for i in np.arange(8):
    arr[i] = i
pprint(arr)
pprint(arr[[7, 6, 1, 2]])
pprint(arr[[-1, -4]])

#########################################################################################################
print('*' * 88)
arr = np.arange(32).reshape((8, 4))
pprint(arr)
pprint(arr[[1, 2, 4, 7], [0, 3, 2, 1]])
pprint(arr[[1, 3, 5, 7]])
pprint(arr[[1, 3, 5, 7]][:, [3, 2, 1, 0]])

#########################################################################################################
print('*' * 88)
# XXXXXXXX转置: 返回底层数据的视图
arr = np.arange(15).reshape((3, 5))
pprint(arr)
# np.transpose(arr)
pprint(arr.T)

arr_ = np.arange(15).reshape((5, 3))
pprint(arr)
pprint(arr_)
pprint(np.dot(arr, arr_))

#########################################################################################################
print('*' * 88)
arr = np.arange(16).reshape((2, 2, 4))
pprint(arr)
# 传入的是轴 (2, 2, 4) (1, 0, 2)
#          (0, 1, 2)
pprint(arr.transpose((1, 0, 2)))

arr_ = arr.swapaxes(1, 2)
pprint(arr_)
pprint(arr_.shape)
