import numpy as np
from pprint import pprint

arr = np.arange(10)
pprint(arr)
pprint(np.sqrt(arr))
pprint(np.exp(arr))

#########################################################################################################
print('*' * 88)
# 二元通用函数:接收两个数组返回一个数组作为结果 add maximum
x = np.random.randn(8)
y = np.random.randn(8)
pprint(x)
pprint(y)

pprint(np.maximum(x, y))

#########################################################################################################
print('*' * 88)
# 通用函数返回多个数组 modf divmod 向量化版本 返回浮点数的小数和整数部分

arr = np.random.randn(7) * 10
pprint(arr)
remainder, whole_part = np.modf(arr)
pprint(remainder)
pprint(whole_part.astype(np.int32))

print(divmod(10.22, 1))

#########################################################################################################
print('*' * 88)
# 通用函数可选参数out
arr = np.arange(8)
pprint(arr)
pprint(np.exp(arr))
pprint(arr)
arr = arr.astype(np.float64)
pprint(arr)
pprint(np.sqrt(arr, arr))
pprint(arr)

#########################################################################################################
print('*' * 88)
# 一元通用数组
arr = 1
print('np.abs(arr)', np.abs(arr))
print('np.fabs(arr)', np.fabs(arr))
print('np.square(arr)', np.square(arr))
print('np.sqrt(arr)', np.sqrt(arr))
print('np.exp(arr)', np.exp(arr))
# 计算每个元素的符号值 正数 1 零 0 负数 -1
print('np.sign(arr)', np.sign(arr))
print('np.ceil(arr)', np.ceil(arr))
print('np.floor(arr)', np.floor(arr))
# 将元素保留到整数位,并保持TYPE
print('np.rint(arr)', np.rint(arr))
print('np.modf(arr)', np.modf(arr))

print('np.isnan(arr)', np.isnan(arr))
print('np.isinf(arr)', np.isinf(arr))
print('np.isfinite(arr)', np.isfinite(arr))

print('np.cos(arr)', np.cos(arr))
print('np.cosh(arr)', np.cosh(arr))
print('np.sin(arr)', np.sin(arr))
print('np.sinh(arr)', np.sinh(arr))
print('np.tan(arr)', np.tan(arr))
print('np.tanh(arr)', np.tanh(arr))
print('np.arcsin(arr)', np.arcsin(arr))
print('np.arccosh(arr)', np.arccosh(arr))
print('np.arcsin(arr)', np.arcsin(arr))
print('np.arcsinh(arr)', np.arcsinh(arr))
print('np.arctan(arr)', np.arctan(arr))
# print('np.arctanh(arr)', np.arctanh(arr))
# 按位取反~arr
print('np.logical_not(arr)', np.logical_not(arr))

#########################################################################################################
print('*' * 88)
# 二元通用数组
x = np.array([1, 2])
y = np.array([3, 4])
print('', np.add(x, y))
print('', np.subtract(x, y))
# 逐元素相乘
print('', np.multiply(x, y))
print('', np.divide(x, y))
print('', np.floor_divide(x, y))
print('', np.power(x, y))
print('', np.maximum(x, y))
# fmax 忽略NaN
print('', np.fmax(x, y))
print('', np.minimum(x, y))
# fmax 忽略NaN
print('', np.fmin(x, y))
# 按元素求模
print('', np.mod(x, y))
# 将第一个数组的符号值改为第二个数组的符号值
print('np.copysign(x, y)', np.copysign(x, y))
# & | ^
print('', np.logical_and(x, y))
print('', np.logical_or(x, y))
print('', np.logical_xor(x, y))
# > >= < <= == !=
print('', np.greater(x, y))
print('', np.greater_equal(x, y))
print('', np.less(x, y))
print('', np.less_equal(x, y))
print('', np.equal(x, y))
print('', np.not_equal(x, y))
