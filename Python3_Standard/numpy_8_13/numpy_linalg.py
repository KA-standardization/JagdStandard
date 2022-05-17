import numpy as np
from pprint import pprint

# numpy中的线性代数 * 是矩阵的逐元素乘法,而不是矩阵的点积
x = np.random.randn(2, 3)
y = np.random.randn(3, 2)
#########################################################################################################
print('*' * 88)

pprint(x)
pprint(y)
# 点积
print('x.dot(y)--> ', end='')
pprint(x.dot(y))
pprint(x @ np.ones(3))

#########################################################################################################
print('*' * 88)
# 求逆
X = np.random.randn(5, 5)
pprint(X)
mat = X.T.dot(X)
pprint(mat)
print('矩阵的逆: ', end='')
pprint(np.linalg.inv(mat))
pprint(mat.dot(np.linalg.inv(mat)).astype(np.int64))

# 行列式求解
q, r = np.linalg.qr(mat)
pprint(q)
pprint(r)

# 将一个方阵的对角元素作为一维数组返回
X = np.random.randn(5, 5)
pprint(X)
print('np.diag')
pprint(np.diag(X))
pprint(np.diag(np.diag(X)))

# 对角元素之和
pprint(np.trace(X))

# 矩阵的行列式
# 一个n×n矩阵的行列式等于其任意行(或列)的元素与对应的代数余子式乘积之和
X = np.array([[1, 2], [3, 4]])
pprint(np.linalg.det(X).astype(np.int32))

# 方阵的特征值和特征向量
# 设 A 是n阶方阵，如果存在数m和非零n维列向量 x，使得 Ax=mx 成立，则称 m 是矩阵A的一个特征值
#
pprint(np.linalg.eig(X))

# Moore-Penrose伪逆
pprint(np.linalg.inv(X))
pprint(np.linalg.pinv(X))

# 奇异值分解
pprint(np.linalg.svd(X))

# 求x 的线性系统 Ax=b 其中A是方阵
# pprint(np.linalg.solve(X,))

# 计算Ax=b的最小二乘解
# pprint(np.linalg.lstsq(X,))

#########################################################################################################
print('*' * 88)
# 正态分布
np.random.seed(1111)  # 全局随机状态
x = np.random.normal(size=(4, 4))
pprint(x)

# 是数据独立于其他随机状态
rng = np.random.RandomState(1234)
pprint(rng.normal(size=(4, 4)))

# 返回一个序列的随机排列 或者返回一个乱序的整数范围序列
pprint(np.random.permutation(x))

# 随机排列一个序列
pprint(x)
np.random.shuffle(x)
pprint(x)

# 从均匀分布中抽取样本
pprint(np.random.rand())

# 从二项分布中抽取样本

pprint(np.random.binomial(10, .5, 100))

# 从beta分布中抽取样本
# pprint(np.random.beta())

# 从卡方分布中抽取样本
# pprint(np.random.chisquare())

# 从伽马分布中抽取样本
# pprint(np.random.gamma())

# 从均匀分布[0,1)分布中抽取样本
# pprint(np.random.uniform())
