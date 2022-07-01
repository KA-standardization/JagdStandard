# 聚类方法 (clustering function)

* 策略
  * 聚类是针对给定的样本,依据它们特征的相似度或距离,将其归并到若干个类或簇中
* 聚类的基本概念
  * **相似度或距离 (similarity or distance)**
    * 聚类的对象是观测数据,或样本集合
    * 假设有$n$个样本,每个样本由$m$个属性的特征向量组成
      * 矩阵$X$表示样本集合
        * $X=[x_{i,j}]_{m\times n}=\left[\begin{matrix}x_{1,1}&x_{1,2}&\cdots&x_{1,n}\\x_{2,1}&x_{2,2}&\cdots&x_{2,n}\\\vdots&\vdots&\vdots&\vdots\\x_{m,1}&x_{m,2}&\cdots&x_{m,n}\end{matrix}\right]$ 
        * 矩阵的第$j$列表示第$j$个样本
          * $j=1,2,\cdots,n$ 
        * 第$i$行表示第$i$个属性
          * $i=1,2,\cdots,m$ 
    * 在聚类中,将样本集合看作是向量空间中点的集合,以该空间的距离表示样本之间的相似度
      * 向量空间
        * 定义
          * 域$F$上的向量空间$V$是满足下面合成法则的集合
            * (a)加法
              * $V\times V\rightarrow V$, 记作$v,w\rightarrow v+w$, 其中$v,w\in V$ 
            * (b)标量乘法
              * $F\times V\rightarrow V$, 记作$c,v\rightarrow cv$, 其中$c\in F,v\in V$ 
        * 这两个合成法则满足下列公理
          * 加法使$V$成为交换群$V^+$, 并带有恒等元,记作0
          * $1v=v$,对所有$v\in V$成立
          * 结合律
            * $(ab)v=a(bv)$
            * 对所有$a,b\in F$, $v\in V$成立
          * 分配律
            * $(a+b)v=av+bv$ 
            * $a(v+w)=av+aw$ 
            * 对所有$a,b\in F$, $v,w\in V$成立
        * 元素在域$F$中的列向量的加法和标量乘法的定义,这样的列向量空间$F^n$构成域$F$上的向量空间
      * **闵可夫斯基距离(Minkowski distance)**
        * 定义
          * 给定样本集合$X$, $X$是$m$维实数向量空间$R^m$中点的集合
            * $x_i,x_j\in X$ 
              * $x_i=(x_{1,i},x_{2,i},\cdots,x_{m,i})^T$ 
              * $x_j=(x_{1,j},x_{2,j},\cdots,x_{m,j})^T$ 
          * 样本$x_i$与样本$x_j$的闵可夫斯基距离为
          * $d_{i,j}=(\sum\limits_{k=1}^m|x_{k,i}-x_{k,j}|^p)^{\frac{1}{p}}$, $p\geq 1$
      * **欧氏距离(Euclidean distance)**
        * 当$p=2$
          - $d_{i,j}=(\sum\limits_{k=1}^m|x_{k,i}-x_{k,j}|^2)^{\frac{1}{2}}$ 
      * **曼哈顿距离(Manhattan distance)**
        - 当$p=1$
          - $d_{i,j}=\sum\limits_{k=1}^m|x_{k,i}-x_{k,j}|$ 
      * **切比雪夫距离(Chebyshev distance)**
        * 当$p=\infty$ 
          * $d_{i,j}=\max\limits_k|x_{k,i}-x_{k,j}|$ 
          * 取各个坐标数值差的绝对值的最大值
      * **马哈拉诺比斯距离(Mahalanobis distance)**
        * 马氏距离,考虑各个分量(特征)之间的相关性并与各个分量的尺度无关
        * 定义
          * 给定一个样本集合$X$, $X=[x_{i,j}]_{m\times n}$, 其协方差矩阵记作$S$ 
          * $d_{i,j}=[(x_i-x_j)^TS^{-1}(x_i-x_j)]^{\frac{1}{2}}$ 
            * $x_i=(x_{1,i},x_{2,i},\cdots,x_{m,i})^T$ 
            * $x_j=(x_{1,j},x_{2,j},\cdots,x_{m,j})^T$ 
        * 当$S$为单位矩阵时,既样本数据的各个分量互相独立且各个分量的方差为1时,马氏距离就是欧式距离
      * **相关系数(correlation coefficient)**
        * 相关系数的绝对值越接近于1,表示样本越相似;越接近于0,表示样本越不相似
        * 定义
          * $r_{i,j}=\frac{\sum\limits_{k=1}^m(x_{k,i}-\overline{x}_i)(x_{k,j}-\overline{x}_j)}{[\sum\limits_{k=1}^m(x_{k,i}-\overline{x}_i)^2\sum\limits_{k=1}^m(x_{k,j}-\overline{x}_j)^2]^{\frac{1}{2}}}$ 
            * $\overline{x}_i=\frac{1}{m}\sum\limits_{k=1}^mx_{k,i}$ 
            * $\overline{x}_j=\frac{1}{m}\sum\limits_{k=1}^mx_{k,j}$ 
      * **夹角余弦(cosine)**
        * 夹角余弦越接近于1,表示样本越相似;越接近于0,表示样本越不相似
        * 定义
          * $s_{i,j}=\frac{\sum\limits_{k=1}^mx_{k,i}x_{k,j}}{[\sum\limits_{k=1}^mx_{k,i}^2\sum\limits_{k=1}^mx_{k,j}^2]^\frac{1}{2}}$ 

  * 类或簇
    * 通过聚类得到的类或簇,本质是样本的子集
    * 硬聚类(hard clustering)
      * 一个聚类方法假定一个样本只能属于一个类,或类的交集为空集
    * 软聚类(soft clustering)
      * 一个聚类方法假定一个样本可以属于多个类,或类的交集不为空集
    * 定义
      * 用$G$表示类或簇
      * 用$x_i,x_j$表示类中的样本
      * 用$n_G$表示$G$中样本的个数
      * 用$d_{i,j}$表示样本$x_i$与样本$x_j$之间的距离
      * (a)设$T$为给定的正数,若集合$G$中任意两个样本$x_i,x_j$, 有
        * $d_{i,j}\leq T$ 
      * (b)设$T$为给定的正数,若对集合$G$的任意样本$x_i$, 一定存在$G$中的另一个样本$x_j$, 使得
        * $d_{i,j}\leq T$ 
      * (c)设$T$为给定的正数,若对集合$G$的任意一个样本$x_i$, $G$中的另一个样本$x_j$, 满足
        * $\frac{1}{n_G-1}\sum\limits_{x_j\in G}d_{i,j}\leq T$ 
      * (d)设$T$和$V$为给定的两个正数,如果集合$G$中任意两个样本$x_i,x_j$的距离$d_{i,j}$, 满足
        * $\frac{1}{n_G(n_G-1)}\sum\limits_{x_i\in G}\sum\limits_{x_j\in G}d_{i,j}\leq T$ 
        * $d_{i,j}\leq V$ 
    * **类的特征**
      * (1)类的均值$\overline{x}_G$, 又称为类的中心
        * $\overline{x}_G=\frac{1}{n_G}\sum\limits_{i=1}^{n_G}x_i$ 
      * (2)类的直径(diameter)$D_G$ 
        * 类的直径$D_G$是类中任意两个样本之间的最大距离
        * $D_G=\max\limits_{x_i,x_j\in G}d_{i,j}$ 
      * (3)类的样本散布矩阵(scatter matrix)$A_G$与样本协方差矩阵(covariance matrix)$S_G$
        * $A_G=\sum\limits_{i=1}^{n_G}(x_i-\overline{x}_G)(x_i-\overline{x}_G)^T$ 
        * $S_G=\frac{1}{m-1}A_G=\frac{1}{m-1}\sum\limits_{i=1}^{n_G}(x_i-\overline{x}_G)(x_i-\overline{x}_G)^T$ 
    * 类与类之间的距离
      * 类$G_p$与类$G_q$之间的距离$D(p,q)$, 也称为连接(linkage)
      * 定义
        * 类$G_p$包含$n_p$个样本
        * 类$G_q$包含$n_q$个样本
        * 用$\overline{x}_p$表示$G_p$的均值,即类的中心
        * 用$\overline{x}_q$表示$G_q$的均值,即类的中心
        * (a)最短距离或单连接(single linkage)
          * 定义类$G_p$的样本与$G_q$的样本之间的最短距离为两类之间的距离
          * $D_{pq}=\min\{d_{i,j}|x_i\in G_p,x_j\in G_q\}$ 
        * (b)最长距离或完全连接(complete linkage)
          * 定义类$G_p$的样本与$G_q$的样本之间的最长距离为两类之间的距离
          * $D_{pq}=\max\{d_{i,j}|x_i\in G_p,x_j\in G_q\}$ 
        * (c)中心距离
          * 定义类$G_p$与类$G_q$的中心$\overline{x}_p$与$\overline{x}_q$之间的距离为两类之间的距离
          * $D_{pq}=d_{\overline{x}_p,\overline{x}_q}$ 
        * (d)平均距离
          * 定义类$G_p$与类$G_q$任意两个样本之间距离的平均值为两类之间的距离
          * $D_{pq}=\frac{1}{n_pn_q}\sum\limits_{x_i\in G_p}\sum\limits_{x_j\in G_q}d_{i,j}$ 

  * 层次聚类

    * 简介
      * 层次聚类假设类别之间存在层次结构,将样本聚到层次化的类中
      * 层次聚类又有聚合(agglomerative)(自下而上bottom-up)聚类, 分列(divisive)(自上而下top-down)聚类两种方法
      * 层次聚类属于hard clustering
    * 策略
      * agglomerative clustering
        * 聚合聚类开始将每个样本各自分到一个类
        * 之后将相距最近的两类合并,建立一个新的类
        * 重复此操作直到满足停止条件,得到层次化的类别
      * divisive clustering
        * 分裂聚类开始将所有样本分到一个类
        * 之后将已有类中相距最远的样本分到两个新的类
        * 重复此操作直到满足停止条件,得到层次化的类别
    * 聚合聚类算法 (agglomerative clustering algorithm)
      * (1)计算$n$个样本两两之间的欧式距离$\{d_{i,j}\}$, 记作矩阵$D=[d_{i,j}]_{n\times n}$ 
      * (2)构造$n$个类,每个类只包含一个样本
      * (3)合并类间距离最小的两个类,其中最短距离为类间距离,构建一个新类
      * (4)计算新类与当前各类的距离,若类的个数为1,终止计算,否则回到(3)步
      * 聚合层次聚类算法的复杂度是$O(n^3m)$ 
        * $n$是样本的个数
        * $m$是样本的维数
    * Examples
      * 给定5个样本的集合,样本之间的欧式距离由如下矩阵$D$表示
        * $D=[d_{i,j}]_{5\times 5}=\left[\begin{matrix}0&7&2&9&3\\7&0&5&4&6\\2&5&0&8&1\\9&4&8&0&5\\3&6&1&5&0\end{matrix}\right]$ 
        * $d_{i,j}$表示第$i$个样本与第$j$个样本之间的欧式距离
      * (1)用5个样本构建5个类
        * $G_i=\{x_i\}$, $i=1,2,3,4,5$ 
        * 样本之间的距离变为类之间的距离,5个类之间的距离矩阵亦为$D$
      * (2)由矩阵$D$可以看出,$D_{3,5}=D_{5,3}=1$为最小
        * $\begin{matrix}&&&&0&&&&\\&&&7&&7&&&\\&&2&&0&&2&&\\&9&&5&&5&&9&\\3&&4&&0&&4&&3\\&6&&8&&8&&6&\\&&1&&0&&1&&\\&&&5&&5&&&\\&&&&0&&&&\\\end{matrix}$ 
        * 把$G_3$和$G_5$合并为一个新类
          * $G_6=\{x_3,x_5\}$ 
      * (3)计算$G_6​$与$G_1,G_2,G_4​$之间的最短距离
        * $D_{6,1}=2$ 
        * $D_{6,2}=5$ 
        * $D_{6,4}=5$ 
        * 其余两类之间的距离是
          * $D_{1,2}=7$ 
          * $D_{1,4}=9$ 
          * $D_{2,4}=4$ 
        * $D_{6,1}=2$最小,所以将$G_1$与$G_6$合并成一个新类
          * $G_7=\{x_1,x_3,x_5\}$ 
      * (4)计算$G_7$与$G_2,G_4$之间的距离
        * $D_{7,2}=5$ 
        * $D_{7,4}=5$ 
        * $D_{2,4}=4$ 
        * 其中$D_{2,4}=4$最小,所以将$G_2$与$G_4$合并成一新类
          * $G_8=\{x_2,x_4\}$ 
      * (5)将$G_7$与$G_8$合并成一个新类
        * $G_9=\{x_1,x_2,x_3,x_4,x_5\}$ 
      * 全部样本聚成1类,聚类终止

  * **$k$均值聚类**

    * $k$均值聚类是基于样本集合划分的聚类算法

      * 将样本集合划分为$k$个子集,构成$k$个类
      * 将$n$个样本分到$k$个类中,每个样本到其所属类的中心距离最小

    * 模型

      * $n$个样本的集合
        * $X=\{x_1,x_2,\cdots,x_n\}$
        * 每个样本由一个特征向量表示,特征向量的维数是$m$
      * $k$个类$G_1,G_2,\cdots,G_k$形成对样本集合$X$的划分
        * $G_i\cap G_j=\varnothing$ 
        * $\bigcup\limits_{i=1}^kG_i=X$ 
      * 用$C$表示划分,一个划分对应着一个聚类结果
        * 划分$C$是一个多对一的函数
        * 如果把每个样本用一个整数表示
          * $i\in\{1,2,\cdots,n\}$ 
        * 每个类也用一个整数表示
          * $l\in \{1,2,\cdots,k\}$ 
        * 划分或者聚类可以用函数
          * $l=C(i)$
      * $k$均值聚类的模型是一个从样本到类的函数

    * 策略

      * $k$均值聚类归结为样本集合$X$的划分,或者从样本到类的函数的选择问题
      * $k$均值聚类的策略是通过损失函数的最小化选取最优的划分或函数$C^*$ 
      * (1)采用欧氏距离平方(squared Euclidean distance)作为样本之间的距离$d(x_i,x_j)$ 
        * $d(x_i,x_j)=\sum\limits_{k=1}^m(x_{k,i}-x_{k,j})^2$ 
          * ​          $=||x_i-x_j||^2$ 
      * (2)定义样本与其所属类的中心之间的距离的总和为损失函数
        * $W(C)=\sum\limits_{l=1}^k\sum\limits_{C(i)=l}||x_i-\overline{x}_l||^2$ 
        * $\overline{x}_l=(\overline{x}_{1,l},\overline{x}_{2,l},\cdots,\overline{x}_{m,l})$是第$l$个类的均值或中心
        * $nl=\sum\limits_{i=1}^nI(C(i)=l)$
          * $I(C(i)=l)$是指示函数,取值为1或0
        * 函数$W(C)$也称为能量
          * 表示相同类中的样本相似度
      * $k$均值问题就是求解最优化问题
        * $C^*=arg\min\limits_CW(C)$ 
          * $=arg\min\limits_C\sum\limits_{l=1}^k\sum\limits_{C(i)=l}||x_i-\overline{x}_l||^2$ 
        * 相似的样本被聚到同类时,损失函数值最小,这个目标函数的最优化能达到聚类的目的
      * $n$个样本分到$k$类,所有可能分法的数目是
        * $S(n,k)=\frac{1}{k!}\sum\limits_{l=1}^k(-1)^{k-l}{k\choose{l}}k^n$, 指数级别
        * $k$均值聚类的最优解求解问题是NP困难问题
        * **二项系数**
          * 符号${n\choose{k}}$表示$n$集合中$k$组合的数目,读作"$n$选$k$"
            * ${n\choose{k}}=\frac{n!}{k!(n-k)!}$ 
          * 此公式对$k$与$n-k$是对称的
            * ${n\choose{k}}={n\choose{n-k}}$ 
          * 这些数出现在二项展开式中,所以称其为二项式系数
            * $(x+y)^n=\sum\limits_{k=0}^n{n\choose{k}}x^ky^{n-k}$ 
          * 二项展开式的一个特例
            * 当$x=y=1$时
              * $2^n=\sum\limits_{k=0}^n{n\choose{k}}$ 
              * 此公式对应于利用二进制$n$串中所含1的个数来计数$2^n$个这类串的过程
                * 因为从$n$个位置中选择$k$个放置1的方法数是${n\choose{k}}$ 
                * 所以有${n\choose{k}}$个二进制$n$串恰好含$k$个1

    * 算法

      * $k$均值聚类的算法是一个迭代过程,每次迭代包括两个步骤
        * (1)选择$k$个类的中心,将样本逐个指派到与其最近的中心的类中,得到一个聚类结果
          * 对给定的中心值$(m_1,m_2,\cdots,m_k)$, 求一个划分$C$, 使得目标函数极小化
            * 在类中心确定的情况下,将每个样本分到一个类中,使样本和其所属类的中心之间的距离总和最小
            * 求解结果,将每个样本指派到与其最近的中心$m_l$的类$G_l$中
            * $\min\limits_C\sum\limits_{l=1}^k\sum\limits_{C(i)=l}||x_i-m_l||^2$ 
        * (2)更新每个类的样本均值,作为类的新中心
          * 对给定的划分$C$, 再求各个类的中心$(m_1,m_2,\cdots,m_k)$,使得目标函数极小化
            * $\min\limits_{m_1,\cdots,m_k}\sum\limits_{l=1}^k\sum\limits_{C(i)=l}||x_i-m_l||^2$ 
            * 在划分确定的情况下,使样本和其所属类的中心之间的距离总和最小,求解结果,对于每个包含$n_l$个样本的类$G_l$,更新其均值$m_l$ 
              * $m_l=\frac{1}{n_l}\sum\limits_{C(i)=l}x_i$, $l=1,2,\cdots,k$ 
        * 重复(1)(2)直至收敛为止
          * 直到划分不再改变,得到聚类结果
      * $k$均值聚类算法 (k-means clustering algorithm)
        * (a)初始化
          * 令$t=0$, 随机选择$k$个样本点作为初始聚类中心
          * $m^{(0)}=(m_1^{(0)},\cdots,m_l^{(0)},\cdots,m_k^{(0)})$ 
        * (b)对样本进行聚类
          * 对固定的类中心
            * $m^{(t)}=(m_1^{(t)},\cdots,m_l^{(t)},\cdots,m_k^{(t)})$ 
            * $m_l^{(t)}$为类$G_l$的中心
          * 计算每个样本到类中心的距离,将每个样本指派到与其最近的中心的类中,构成聚类结果$C^{(t)}$ 
        * (c)计算新的类中心
          * 对聚类结果$C^{(t)}$,计算当前各个类中的样本的均值,作为新的类中心
            * $m^{(t+1)}=(m_1^{(t+1)},\cdots,m_l^{(t+1)},\cdots,m_k^{(t+1)})$ 
        * (d)如果迭代收敛或符合停止条件
          * 输出$C^*=C^{(t)}$ 
          * 否则
            * 令$t=t+1$, 返回第(b)步

    * Example

      * 给定含有5个样本的集合

        * $X=\left[\begin{matrix}0&0&1&5&5\\2&0&0&0&2\end{matrix}\right]$ 

        * 将样本聚到2个类中

        * ```python
          # import
          import warnings
          warnings.filterwarnings('ignore')
          import numpy as np
          X1=np.array((0,2)).T
          X2=np.array((0,0)).T
          X3=np.array((1,0)).T
          X4=np.array((5,0)).T
          X5=np.array((5,2)).T
          ```

      * (a)选择两个样本点作为类的中心

        * $m_1^{(0)}=x_1=(0,2)^T$ 
        * $m_2^{(0)}=x_2=(0,0)^T$ 

      * (b)以$m_1^{(0)},m_2^{(0)}$为类$G_1^{(0)},G_2^{(0)}$的中心

        * 计算

          * $x_3=(1,0)^T$ 
          * $x_4=(5,0)^T$ 
          * $x_5=(5,2)^T$ 

        * 与

          * $m_1^{(0)}=x_1=(0,2)^T$ 
          * $m_2^{(0)}=x_2=(0,0)^T$ 
          * 的欧氏距离平方

        * ```python
          def euclidean_distance2(x1,x2):
              res=[]
              for i in range(len(x1)):
                  res.append((x1[i]-x2[i])**2)
              return sum(res)
          ```

        * 对$x_3=(1,0)^T​$

          * $d(x_3,m_1^{(0)})=5$ 

          * $d(x_3,m_2^{(0)})=1$

          * 将$x_3$分到类$G_2^{(0)}$ 

          * ```python
            display(euclidean_distance2(X3,X1))
            display(euclidean_distance2(X3,X2))
            ```

        * 对$x_4=(5,0)^T$

          - $d(x_4,m_1^{(0)})=29$  

          - $d(x_4,m_2^{(0)})=25$ 

          - 将$x_4$分到类$G_2^{(0)}$ 

          - ```python
            display(euclidean_distance2(X4,X1))
            display(euclidean_distance2(X4,X2))
            ```

        * 对$x_5=(5,2)^T$

          - $d(x_5,m_1^{(0)})=25$ 

          - $d(x_5,m_2^{(0)})=29$ 

          - 将$x_5$分到类$G_1^{(0)}$ 

          - ```python
            display(euclidean_distance2(X5,X1))
            display(euclidean_distance2(X5,X2))
            ```

      * (c)得到新类

        * $G_1^{(1)}=\{x_1,x_5\}$ 

        * $G_2^{(1)}=\{x_2,x_3,x_4\}$ 

        * 计算类的中心

          * ```python
            def class_mean(*args):
                if len(args)<1:
                    return None
                temp=[]
                for i in range(len(args)):
                    temp.append(args[i])
                mean=[]
                count=0
                for j in range(len(temp[0])):
                    for v in temp:
                        count+=v[j]
                    mean.append(count)
                    count=0
                res=[]
                for k in range(len(mean)):
                    res.append(mean[k]/len(args))      
                return res  
            ```

          * $m_1^{(1)}=(2.5,2.0)^T$ 

            * ```python
              tuple(class_mean(X1,X5))
              ```

          * $m_2^{(1)}=(2,0)^T$ 

            * ```python
              tuple(class_mean(X2,X3,X4))
              ```

      * (d)重复步骤(b)和(c)

        * 将$x_1$分到类$G_1^{(1)}$ 
        * 将$x_2$分到类$G_2^{(1)}$ 
        * 将$x_3$分到类$G_2^{(1)}$ 
        * 将$x_4$分到类$G_2^{(1)}$ 
        * 将$x_5$分到类$G_1^{(1)}$ 
        * 得到新类
          * $G_1^{(2)}=\{x_1,x_5\}$ 
          * $G_2^{(2)}=\{x_2,x_3,x_4\}$ 
        * 由于得到新类没有改变,聚类停止
          * 得到结果
            * $C_1^*=\{x_1,x_5\}$ 
            * $C_2^*=\{x_2,x_3,x_4\}$ 

    * 总结

      * 选择不同的初始中心,会得到不同的聚类结果
      * 对于初始中心的选择,可以用层次聚类对样本进行聚类,得到$k$个类时停止,然后从每个类中选取一个与中心距离最近的点
      * $k$值得选择,聚类结果的质量可以用类的平均直径来衡量
        * 类别变小时,平均直径会增加
        * 类别数变大超过某个值以后,平均直径会不表
        * 这个值是最优的$k$值
