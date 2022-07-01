# Python实现部分机器学习算法

## 1.kdtree

```python
#导入必要的编程包
import random
from copy import deepcopy
from time import time
import numpy as np
from numpy.linalg import norm
from collections import Counter
#给定数据
Counter([0, 1, 1, 2, 2, 3, 3, 4, 3, 3]).most_common(1)

def partition_sort(arr, k, key=lambda x: x):
    """
    以枢纽(位置k)为中心将数组划分为两部分, 枢纽左侧的元素不大于枢纽右侧的
元素
    :param arr: 待划分数组
    :param p: 枢纽前部元素个数
    :param key: 比较方式
    :return: 无
    """
    start, end = 0, len(arr) - 1
    assert 0 <= k <= end
    while True:
        i, j, pivot = start, end, deepcopy(arr[start])
        while i < j:
            # 从右向左查找较小元素
            while i < j and key(pivot) <= key(arr[j]):
                j -= 1
            if i == j: break
            arr[i] = arr[j]
            i += 1
            # 从左向右查找较大元素
            while i < j and key(arr[i]) <= key(pivot):
                i += 1
            if i == j: break
            arr[j] = arr[i]
            j -= 1
        arr[i] = pivot
        if i == k:
            return
        elif i < k:
            start = i + 1
        else:
            end = i - 1

def max_heapreplace(heap, new_node, key=lambda x: x[1]):
    """
    大根堆替换堆顶元素
    :param heap: 大根堆/列表
    :param new_node: 新节点
    :return: 无
    """
    heap[0] = new_node
    root, child = 0, 1
    end = len(heap) - 1
    while child <= end:
        if child < end and key(heap[child]) < key(heap[child + 1]):
            child += 1
        if key(heap[child]) <= key(new_node):
            break
        heap[root] = heap[child]
        root, child = child, 2 * child + 1
    heap[root] = new_node

def max_heappush(heap, new_node, key=lambda x: x[1]):
    """
    大根堆插入元素
    :param heap: 大根堆/列表
    :param new_node: 新节点
    :return: 无
    """
    heap.append(new_node)
    pos = len(heap) - 1
    while 0 < pos:
        parent_pos = pos - 1 >> 1
        if key(new_node) <= key(heap[parent_pos]):
            break
        heap[pos] = heap[parent_pos]
        pos = parent_pos
    heap[pos] = new_node

#需要初始化一个Node类，表示KD树中的一个节点，主要包括节点本身的data值，以及其左右子节点
class KDNode(object):
    """kd树节点"""
    def __init__(self, data=None, label=None, left=None, right=None, axis=None, parent=None):
        """
        构造函数
        :param data: 数据
        :param label: 数据标签
        :param left: 左孩子节点
        :param right: 右孩子节点
        :param axis: 分割轴
        :param parent: 父节点
        """
        self.data = data
        self.label = label
        self.left = left
        self.right = right
        self.axis = axis
        self.parent = parent

class KDTree(object):
    """kd树"""
    def __init__(self, X, y=None):
        """
        构造函数
        :param X: 输入特征集, n_samples*n_features
        :param y: 输入标签集, 1*n_samples
        """
        self.root = None
        self.y_valid = False if y is None else True
        self.create(X, y)

    def create(self, X, y=None):
        """
        构建kd树
        :param X: 输入特征集, n_samples*n_features
        :param y: 输入标签集, 1*n_samples
        :return: KDNode
        """
        def create_(X, axis, parent=None):
            """
            递归生成kd树

            :param X: 合并标签后输入集
            :param axis: 切分轴
            :param parent: 父节点
            :return: KDNode
            """
            n_samples = np.shape(X)[0]
            if n_samples == 0:
                return None
            mid = n_samples >> 1
            partition_sort(X, mid, key=lambda x: x[axis])
            if self.y_valid:
                kd_node = KDNode(X[mid][:-1], X[mid][-1], axis=axis, parent=parent)
            else:
                kd_node = KDNode(X[mid], axis=axis, parent=parent)
            next_axis = (axis + 1) % k_dimensions
            kd_node.left = create_(X[:mid], next_axis, kd_node)
            kd_node.right = create_(X[mid + 1:], next_axis, kd_node)
            return kd_node
        print('building kd-tree...')
        k_dimensions = np.shape(X)[1]
        if y is not None:
            X = np.hstack((np.array(X), np.array([y]).T)).tolist()
        self.root = create_(X, 0)

    def search_knn(self, point, k, dist=None):
        """
        kd树中搜索k个最近邻样本
        :param point: 样本点
        :param k: 近邻数
        :param dist: 度量方式
        :return:
        """

        def search_knn_(kd_node):
            """
            搜索k近邻节点
            :param kd_node: KDNode
            :return: None
            """
            if kd_node is None:
                return
            data = kd_node.data
            distance = p_dist(data)
            if len(heap) < k:
                # 向大根堆中插入新元素
                max_heappush(heap, (kd_node, distance))
            elif distance < heap[0][1]:
                # 替换大根堆堆顶元素
                max_heapreplace(heap, (kd_node, distance))
            axis = kd_node.axis
            if abs(point[axis] - data[axis]) < heap[0][1] or len(heap) < k:
                # 当前最小超球体与分割超平面相交或堆中元素少于k个
                search_knn_(kd_node.left)
                search_knn_(kd_node.right)
            elif point[axis] < data[axis]:
                search_knn_(kd_node.left)
            else:
                search_knn_(kd_node.right)
        if self.root is None:
            raise Exception('kd-tree must be not null.')
        if k < 1:
            raise ValueError("k must be greater than 0.")
        # 默认使用2范数度量距离
        if dist is None:
            p_dist = lambda x: norm(np.array(x) - np.array(point))
        else:
            p_dist = lambda x: dist(x, point)
        heap = []
        search_knn_(self.root)
        return sorted(heap, key=lambda x: x[1])

    def search_nn(self, point, dist=None):
        """
        搜索point在样本集中的最近邻
        :param point:
        :param dist:
        :return:
        """
        return self.search_knn(point, 1, dist)[0]

    def pre_order(self, root=KDNode()):
        """先序遍历"""
        if root is None:
            return
        elif root.data is None:
            root = self.root
        yield root
        for x in self.pre_order(root.left):
            yield x
        for x in self.pre_order(root.right):
            yield x

    def lev_order(self, root=KDNode(), queue=None):
        """层次遍历"""
        if root is None:
            return
        elif root.data is None:
            root = self.root
        if queue is None:
            queue = []
        yield root
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        if queue:
            for x in self.lev_order(queue.pop(0), queue):
                yield x

    @classmethod
    def height(cls, root):
        """kd-tree深度"""
        if root is None:
            return 0
        else:
            return max(cls.height(root.left), cls.height(root.right)) + 1


class KNeighborsClassifier(object):
    """K近邻分类器"""

    def __init__(self, k, dist=None):
        """构造函数"""
        self.k = k
        self.dist = dist
        self.kd_tree = None

    def fit(self, X, y):
        """建立kd树"""
        print('fitting...')
        X = self._data_processing(X)
        self.kd_tree = KDTree(X, y)

    def predict(self, X):
        """预测类别"""
        if self.kd_tree is None:
            raise TypeError('Classifier must be fitted before predict!')
        search_knn = lambda x: self.kd_tree.search_knn(point=x, k=self.k, dist=self.dist)
        y_ptd = []
        X = (X - self.x_min) / (self.x_max - self.x_min)
        for x in X:
            y = Counter(r[0].label for r in search_knn(x)).most_common(1)[0][0]
            y_ptd.append(y)
        return y_ptd

    def score(self, X, y):
        """预测正确率"""
        y_ptd = self.predict(X)
        correct_nums = len(np.where(np.array(y_ptd) == np.array(y))[0])
        return correct_nums / len(y)

    def _data_processing(self, X):
        """数据归一化"""
        X = np.array(X)
        self.x_min = np.min(X, axis=0)
        self.x_max = np.max(X, axis=0)
        X = (X - self.x_min) / (self.x_max - self.x_min)
        return X

## 代码测试
if __name__ == '__main__':
    """测试程序正确性
    使用kd-tree和计算全部距离, 比对两种结果是否一致"""
    N = 100000
    X = [[np.random.random() * 100 for _ in range(3)] for _ in range(N)]
    kd_tree = KDTree(X)

    for x in X[:10]:
        res1 = ([list(node[0].data) for node in kd_tree.search_knn(x, 20)])
        distances = norm(np.array(X) - np.array(x), axis=1)
        res2 = ([list(X[i]) for _, i in sorted(zip(distances, range(N)))[:20]])
        if all(x in res2 for x in res1):
            print('correct ^_^ ^_^')
        else:
            print('error >_< >_<')
    print('\n')

    """10万个样本集中查找10个实例的最近邻"""
    n = 10
    indices = random.sample(range(N), n)
    # 1、kd-tree搜索, 0.19251227378845215s
    tm = time()
    for i, index in enumerate(indices):
        kd_tree.search_nn(X[index])
    print('kd-tree search: {}s'.format(time() - tm))

    # 2、numpy计算全部样本与新实例的距离, 0.5163719654083252s
    tm = time()
    for i, index in enumerate(indices):
        min(norm(X - np.array(X[index]), axis=0))
    print('numpy search: {}s'.format(time() - tm))

    # 3、python循环计算距离, 7.144993782043457s
    tm = time()
    for i, index in enumerate(indices):
        min([norm(np.array(X[index]) - np.array(x)) for x in X])
    print('python search: {}s'.format(time() - tm))
    print()

if __name__ == '__main__':
    """模型测试"""
    X, y = [], []
    
    
    #数据不存在
    #X 需要自己找特征数据
    #y

    """训练误差"""
    knc = KNeighborsClassifier(10)
    knc.fit(X, y)
    print(knc.score(X, y))  # 0.963
    print()

    """测试误差"""
    X_train, X_test = X[:980], X[-20:]
    y_train, y_test = y[:980], y[-20:]
    knc = KNeighborsClassifier(10)
    knc.fit(X_train, y_train)
    print(knc.score(X_test, y_test))  # 1.0

```

## 2.SVD(降维)

```python
import numpy as np 
class CSVD(object):
    '''
    实现svd分解降维应用示例的Python代码
    '''    
    def __init__(self, data):
        self.data = data       #用户数据
        self.S = []  #用户数据矩阵的奇异值序列 singular values
        self.U = []  #svd后的单位正交向量
        self.VT = []  #svd后的单位正交向量
        self.k = 0   #满足self.p的最小k值(k表示奇异值的个数)
        self.SD = [] #对角矩阵，对角线上元素是奇异值 singular values diagonal matrix        
    def _svd(self):
        '''
        用户数据矩阵的svd奇异值分解
        '''
        self.U, self.S, self.VT = np.linalg.svd(self.data)
        return self.U, self.S, self.VT        
    def _calc_k(self, percentge):
    '''确定k值：前k个奇异值的平方和占比 >=percentage, 求满足此条件的最小k值
        :param percentage, 奇异值平方和的占比的阈值
        :return 满足阈值percentage的最小k值
        '''
        self.k = 0
        #用户数据矩阵的奇异值序列的平方和
        total = sum(np.square(self.S))
        svss = 0 #奇异值平方和 singular values square sum
        for i in range(np.shape(self.S)[0]):
            svss += np.square(self.S[i])
            if (svss/total) >= percentge:
                self.k = i+1
                break
        return self.k
 
    def _buildSD(self, k):
        '''构建由奇异值组成的对角矩阵
        :param k,根据奇异值开放和的占比阈值计算出来的k值
        :return 由k个前奇异值组成的对角矩阵
        '''
        #方法1：用数组乘方法
        self.SD = np.eye(self.k) * self.S[:self.k] 
        #方法2：用自定义方法
        e = np.eye(self.k)
        for i in range(self.k):
            e[i,i] = self.S[i] 
        return self.SD
    
    def DimReduce(self, percentage):
        '''
        SVD降维
        :param percentage, 奇异值开方和的占比阈值
        :return 降维后的用户数据矩阵
        '''
        #Step1:svd奇异值分解
        self._svd()
        #Step2:计算k值
        self._calc_k(percentage)
        print('\n按照奇异值开方和占比阈值percentage=%d, 求得降维的k=%d'%(percentage, self.k))
        #Step3:构建由奇异值组成的对角矩阵singular values diagonal
        self._buildSD(self.k)
        k,U,SD,VT = self.k,self.U, self.SD, self.VT
        #Step4:按照svd分解公式对用户数据矩阵进行降维，得到降维压缩后的数据矩阵        
        a = U[:len(U), :k]
        b = np.dot(SD, VT[:k, :len(VT)])
        newData = np.dot(a,b)
        return newData
        
def CSVD_manual():
    ##训练数据集，用户对商品的评分矩阵，行为多个用户对单个商品的评分，列为用户对每个商品的评分
    data = np.array([[5, 5, 0, 5],
                     [5, 0, 3, 4],
                     [3, 4, 0, 3],
                     [0, 0, 5, 3],
                     [5, 4, 4, 5],
                     [5, 4, 5, 5]])
    percentage = 0.9
    svdor = CSVD(data)
    ret = svdor.DimReduce(percentage)
    print('====================================================')
    print('原始用户数据矩阵:\n', data)
    print('降维后的数据矩阵:\n', ret)
    print('====================================================')    
if __name__=='__main__':
    CSVD_manual()

```

## 3.因子分解机(FM)(逻辑回归升级)

```python
import numpy as np
def stocGradAscent(dataMatrix, classLabels, k, max_iter, alpha):
    '''利用随机梯度下降法训练FM模型
    input:  dataMatrix(mat)特征
            classLabels(mat)标签
            k(int)v的维数
            max_iter(int)最大迭代次数
            alpha(float)为随机梯度下降法的学习率
    output: w0(float),w(mat),v(mat):权重
    '''
    m, n = np.shape(dataMatrix)
    # 1、初始化参数
    w = np.zeros((n, 1))  # 其中n是特征的个数
    w0 = 0  # 偏置项
    v = initialize_v(n, k)  # 初始化V
    
    # 2、训练
    for it in range(max_iter):
        for x in range(m):  # 随机优化，对每一个样本而言的
            inter_1 = dataMatrix[x] * v
            inter_2 = np.multiply(dataMatrix[x], dataMatrix[x]) * \
             np.multiply(v, v)  # multiply对应元素相乘
            # 完成交叉项
            interaction = np.sum(np.multiply(inter_1, inter_1) - inter_2) / 2.
            p = w0 + dataMatrix[x] * w + interaction  # 计算预测的输出
            loss = sigmoid(classLabels[x] * p[0, 0]) - 1
        
            w0 = w0 - alpha * loss * classLabels[x]
            for i in range(n):
                if dataMatrix[x, i] != 0:
                    w[i, 0] = w[i, 0] - alpha * loss * classLabels[x] * dataMatrix[x, i]
                    
                    for j in range(k):
                        v[i, j] = v[i, j] - alpha * loss * classLabels[x] * \
                        (dataMatrix[x, i] * inter_1[0, j] -\
                          v[i, j] * dataMatrix[x, i] * dataMatrix[x, i])
        
        # 计算损失函数的值
        if it % 1000 == 0:
            print ("\t------- iter: ", it, " , cost: ",             getCost(getPrediction(np.mat(dataMatrix), w0, w, v), classLabels)))
    
    # 3、返回最终的FM模型的参数
    return w0, w, v

def initialize_v(n, k):
    '''初始化交叉项
    input:  n(int)特征的个数
            k(int)FM模型的超参数
    output: v(mat):交叉项的系数权重
    '''
    v = np.mat(np.zeros((n, k)))    
    for i in range(n):
        for j in range(k):
            # 利用正态分布生成每一个权重
            v[i, j] = normalvariate(0, 0.2)
    return v

from random import normalvariate

def sigmoid(inx):
	return 1.0/(1+np.exp(-inx))

def getCost(predict, classLabels):
    '''计算预测准确性
    input:  predict(list)预测值
            classLabels(list)标签
    output: error(float)计算损失函数的值
    '''
    m = len(predict)
    error = 0.0
    for i in range(m):
        error -=  np.log(sigmoid(predict[i] * classLabels[i] ))  
    return error

```

## 4.softmax回归(多分类)

```python
import numpy as np
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

def load_data():
     digits = load_digits()
     data = digits.data
     label = digits.target
     return np.mat(data), label

def gradient_descent(train_x, train_y, k, maxCycle, alpha):
# k 为类别数
     numSamples, numFeatures = np.shape(train_x)
     weights = np.mat(np.ones((numFeatures, k)))
     
     for i in range(maxCycle):
          value = np.exp(train_x * weights)  
          rowsum = value.sum(axis = 1)   # 横向求和
          rowsum = rowsum.repeat(k, axis = 1)  # 横向复制扩展
          err = - value / rowsum  #计算出每个样本属于每个类别的概率
          for j in range(numSamples):     
               err[j, train_y[j]] += 1
          weights = weights + (alpha / numSamples) * (train_x.T * err)
     return weights  

def test_model(test_x, test_y, weights):
     results = test_x * weights
     predict_y = results.argmax(axis = 1)
     count = 0
     for i in range(np.shape(test_y)[0]):
          if predict_y[i,] == test_y[i,]:
               count += 1   
     return count / len(test_y), predict_y 

if __name__ == "__main__":
     data, label = load_data()
     #data = preprocessing.minmax_scale(data, axis = 0)
     #数据处理之后识别率降低了
     train_x, test_x, train_y, test_y = train_test_split(data, label, test_size = 0.25, random_state=33)
     k = len(np.unique(label))     
     weights = gradient_descent(train_x, train_y, k, 800, 0.01)
     accuracy, predict_y = test_model(test_x, test_y, weights)
     print("Accuracy:", accuracy)

```

## 5.DBSCAN

```python
import math
import numpy as np
import pylab as pl  #可以使用plt代替
#数据集：每三个是一组分别是西瓜的编号，密度，含糖量
data = """
1,0.697,0.46,2,0.774,0.376,3,0.634,0.264,4,0.608,0.318,5,0.556,0.215,
6,0.403,0.237,7,0.481,0.149,8,0.437,0.211,9,0.666,0.091,10,0.243,0.267,
11,0.245,0.057,12,0.343,0.099,13,0.639,0.161,14,0.657,0.198,15,0.36,0.37,
16,0.593,0.042,17,0.719,0.103,18,0.359,0.188,19,0.339,0.241,20,0.282,0.257,
21,0.748,0.232,22,0.714,0.346,23,0.483,0.312,24,0.478,0.437,25,0.525,0.369,
26,0.751,0.489,27,0.532,0.472,28,0.473,0.376,29,0.725,0.445,30,0.446,0.459"""
#数据处理 dataset是30个样本（密度，含糖量）的列表
a = data.split(',')
dataset = [(float(a[i]), float(a[i+1])) for i in range(1, len(a)-1, 3)]
#计算欧几里得距离,a,b分别为两个元组
def dist(a, b):
    return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))
#算法模型
def DBSCAN(D, e, Minpts):
    #初始化核心对象集合T,聚类个数k,聚类集合C, 未访问集合P,
    T = set(); k = 0; C = []; P = set(D)
    for d in D:
        if len([ i for i in D if dist(d, i) <= e]) >= Minpts:
            T.add(d)
    #开始聚类
    while len(T):
        P_old = P
        o = list(T)[np.random.randint(0, len(T))]
        P = P - set(o)
        Q = []; Q.append(o)
        while len(Q):
            q = Q[0]
            Nq = [i for i in D if dist(q, i) <= e]
            if len(Nq) >= Minpts:
                S = P & set(Nq)
                Q += (list(S))
                P = P - S
            Q.remove(q)
        k += 1
        Ck = list(P_old - P)
        T = T - set(Ck)
        C.append(Ck)
    return C
#画图
def draw(C):
    colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
    for i in range(len(C)):
        coo_X = []    #x坐标列表
        coo_Y = []    #y坐标列表
        for j in range(len(C[i])):
            coo_X.append(C[i][j][0])
            coo_Y.append(C[i][j][1])
        pl.scatter(coo_X, coo_Y, marker='x', color=colValue[i%len(colValue)], label=i)

    pl.legend(loc='upper right')
    pl.show()
C = DBSCAN(dataset, 0.11, 5)
draw(C)

```

## 6.贝叶斯

```python
# coding=utf-8
#朴素贝叶斯原生代码实现
import numpy as np

def loaddata():
    X = np.array([[1,'S'],[1,'M'],[1,'M'],[1,'S'],
         [1, 'S'], [2, 'S'], [2, 'M'], [2, 'M'],
         [2, 'L'], [2, 'L'], [3, 'L'], [3, 'M'],
         [3, 'M'], [3, 'L'], [3, 'L']])
    y = np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])
    return X, y

def Train(trainset,train_labels):
    m = trainset.shape[0] #数据量
    n = trainset.shape[1] #特征数
    prior_probability = {}# 先验概率 key是类别值，value是类别的概率值
    conditional_probability ={}# 条件概率 key的构造：类别，特征,特征值
    labels = set(train_labels)
    # 计算先验概率(此时没有除以总数据量m)
    for label in labels:
        prior_probability[label] = len(y[y == label])

    #计算条件概率
    for i in range(m):
        for j in range(n):
            # key的构造：类别，特征,特征值
            key = str(y[i])+','+str(j)+','+str(trainset[i][j])
            if key in conditional_probability:
                conditional_probability[key] += 1
            else:
                conditional_probability[key] = 1

    conditional_probability_final = {}#因字典在循环时不能改变，故定义新字典保存值
    for key in conditional_probability:
        label = key.split(',')[0]
        #拉普拉斯修正
        key1 = int(key.split(',')[1])
        Ni = len(set(trainset[:,key1]))
        conditional_probability_final[key] = (conditional_probability[key]+1)/(prior_probability[int(label)]+Ni)

    # 最终的先验概率(此时除以总数据量m)
    for label in labels:
        #拉普拉斯修正防止0概率化
        prior_probability[label] = (prior_probability[label]+1)/(m+len(labels))
    return prior_probability,conditional_probability_final,labels
def predict(data):
    result={}
    for label in train_labels_set:
        temp=1.0
        for j in range(len(data)):
            key = str(label)+','+str(j)+','+str(data[j])
            temp = temp*conditional_probability[key]
        result[label] = temp * prior_probability[label]
    print('result=',result)

    return sorted(result.items(), key=lambda x: x[1],reverse=True)[0][0]
X,y = loaddata()
prior_probability,conditional_probability,train_labels_set = Train(X,y)

print('prior_probability='+str(prior_probability))
print('conditional_probability='+str(conditional_probability))
y_hat = predict([2,'S'])
print('y_hat=',y_hat)
```



