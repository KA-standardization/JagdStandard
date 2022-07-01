# 朴素贝叶斯法(naive Bayes algorithm)

* **当事实改变,我的观念也跟着改变**
* **Abstract**
  * (1) 首先基于特征条件独立,假设学习输入输出的联合概率分布
  * (2) 对给定的输入,利用贝叶斯定理求出后验概率最大的输出
  * 先验概率 (不确定性)
    - 把对事件$A$发生的信念记为$P(A)$ 
  * 后验概率
    - 把得到证据$X$后,$A$事件的概率记为$P(A|X)$ 

#### 朴素贝叶斯法的学习与分类

* $x\in \cal X\rm \subseteq R^n$ 
  * $x$为输入特征向量
  * $\cal X$为$n$维向量的集合
* $y\in \cal Y \rm =\{c_1,c_2,\cdots,c_K\}$ 
  * $y$为输出类标记 (class label)
  * $\cal Y$为类标记集合
* $X$是定义在输入空间$\cal X$上的随机向量,$Y$是定义在输出空间$\cal Y$上的随机变量
* $P(X,Y)$是$X$和$Y$的联合概率分布
* 由$P(X,Y)$独立同分布产生,训练数据集
  * $T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$ 
* 朴素贝叶斯法通过训练数据集学习联合概率分布$P(X,Y)$ 
  * 先验概率分布
    * $P(Y=c_k)$, $k=1,2,\cdots,K$ 
  * 条件概率分布
    * $P(X=x|Y=c_k)=P(X^{(1)}=x^{(1)},\cdots,X^{(n)}=x^{(n)}|Y=c_k)$, $k=1,2,\cdots,K$ 
    * **条件概率**
      * 定义
        * 设$E$和$F$是具有$P(F)>0$的事件,给定$F$的条件下$E$的条件概率记作$P(E|F)$
          * $P(E|F)=\frac{P(E\cap F)}{P(F)}$ 
      * 一般来说,为了找出给定$F$的条件下$E$的条件概率,我们用$F$作为样本空间.作为要出现$E$的一个结果,这个结果也必须属于$E\cap F$ 
  * 条件独立性假设
    * $P(X=x|Y=c_k)=P(X^{(1)}=x^{(1)},\cdots,X^{(n)}=x^{(n)}|Y=c_k)$ 
    * ​                                  $=\prod\limits_{j=1}^nP(X^{(j)}=x^{(j)}|Y=c_k)$ 
    * 条件独立性假设等于说用于分类的特征在类确定的条件下都是条件独立的
      * 有时会牺牲一定的准确性
    * **独立性**
      - 定义
        - 概率为0的事件是指独立于所有事件(包括它自己)的事件
        - 如果$P[B]\not=0$,那么事件$A$独立于事件$B$当且仅当$P[A|B]=P[A]$ 
          - 如果知道$B$发生不会改变$A$发生的概率,那么$A$和$B$是独立的
        - 不相交的事件不可能是独立的(除非其中一个事件的概率为0)
      - 定理
        - $A$独立于$B$,当且仅当$P[A\cap B]=P[A]\cdot P[B]$
        - 具有对称性,即$A$独立于$B$,与$B$独立于$A$是一样的
        - 推论
          - $A$独立于$B$当且仅当$B$独立于$A$ 
  * 分类
    * 对给定输入$x$,通过学习到的模型计算后验概率分布$P(Y=c_k|X=x)$,将后验概率最大的类作为$x$的类输出
    * 根据贝叶斯定理
      * $P(Y=c_k|X=x)=\frac{P(X=x|Y=c_k)P(Y=c_k)}{\sum\limits_kP(X=x|Y=c_k)P(Y=c_k)}$ 
      * ​                                  $=\frac{P(Y=c_k)\prod\limits_{j=1}P(X^{(j)}=x^{(j)}|Y=c_k)}{\sum\limits_kP(Y=c_k)\prod\limits_{j=1}P(X^{(j)}=x^{(j)}|Y=c_k)}$, $k=1,2,\cdots,K$ 
      * **贝叶斯定理**
        * 定理
          * 假设$E$和$F$是样本空间$S$的两个事件,且$P(E)\not=0$,$P(F)\not=0$,则
            * $P(F|E)=\frac{P(E|F)P(F)}{P(E|F)P(F)+P(E|\overline{F})P(\overline{F})}$ 
          * 证明1
            * 由条件概率
              * $P(E|F)=\frac{P(E\cap F)}{P(F)}$ 及$P(F|E)=\frac{P(F\cap E)}{P(E)}$ 
            * 有
              * $P(E\cap F)=P(F|E)P(E)$及$P(E\cap F)=P(E|F)P(F)$ 
            * 得
              * $P(F|E)P(E)=P(E|F)P(F)$ 
            * 两边同时除以$P(E)$
              * $P(F|E)=\frac{P(E|F)P(F)}{P(E)}$ 
          * 证明2
            * 由
              * $E=E\cap S=E\cap (F\cup \overline{F})=(E\cap F)\cup(E\cap\overline{F})$ 
              * $E\cap F$与$E\cap \overline{F}$不相交
            * 有
              * $P(E)=P(E\cap F)+P(E\cap \overline{F})$ 
            * 由
              * $P(E\cap F)=P(E|F)P(F)$ 
              * $P(E\cap \overline{F})=P(E|\overline{F})P(\overline{F})$ 
                * $P(E|\overline{F})=\frac{P(E\cap\overline{F})}{P(\overline{F})}$ 
            * 得
              * $P(E)=P(E\cap F)+P(E\cap \overline{F})=P(E|F)P(F)+P(E|\overline{F})P(\overline{F})$
        * 扩展贝叶斯定理
          * 假设$E$是取自样本空间$S$的事件,$F_1,F_2,\cdots,F_n$是互斥事件,且$\bigcup\limits_{i=1}^nF_i=S$ 
          * 假定$P(E)\not=0$, $P(F_i)\not=0$, $i=1,2,\cdots,n$
            * $P(F_j|E)=\frac{P(E|F_j)P(F_j)}{\sum\limits_{i=1}^nP(E|F_i)P(F_i)}$ 
    * 朴素贝叶斯分类器为
      * $y=f(x)=arg\max\limits_{c_k}\frac{P(Y=c_k)\prod\limits_{j=1}P(X^{(j)}=x^{(j)}|Y=c_k)}{\sum\limits_kP(Y=c_k)\prod\limits_{j=1}P(X^{(j)}=x^{(j)}|Y=c_k)}$ 
      * 因分母对所有$c_k$都是相同的,有
        * $y=arg\max\limits_{c_k}P(Y=c_k)\prod\limits_jP(X^{(j)}=x^{(j)}|Y=c_k)$ 
    * 朴素贝叶斯将实例分到后验概率最大的类中,等价于期望风险最小化
      * 损失函数
        * $0-1$ loss function
          * $L(Y,f(X))=\begin{cases}1,Y\not=f(X)\\0,Y=f(X)\end{cases}$ ,$f(X)$是分类决策函数
      * 期望风险函数
        * $R_{exp}(f)=E[L(Y,f(X))]$ 
      * 期望取联合分布$P(X,Y)$,因此取条件期望
        * $R_{exp}(f)=E_X\sum\limits_{k=1}^K[L(c_k,f(X))]P(c_k|X)$ 
      * 使期望风险最小化,需对$X=x$逐个极小化
        * $f(x)=arg\min\limits_{y\in \cal Y}\sum\limits_{k=1}^KL(c_k,y)P(c_k|X=x)$ 
        * ​          $=arg\min\limits_{y\in \cal Y}\sum\limits_{k=1}^KP(y\not=c_k|X=x)$ 
        * ​          $=arg\min\limits_{y\in \cal Y}(1-P(y=c_k|X=x))$ 
        * ​          $=arg\max\limits_{y\in \cal Y}P(y=c_k|X=x)$ 
      * **根据期望风险最小化准则就得到了后验概率最大化准则**
        * $f(x)=arg\max\limits_{c_k}P(c_k|X=x)$ 
      * **期望**
        * 随机变量的期望(expectation)或期望值(expected value)又称均值(mean)或平均数(average)
        * 一个随机变量的期望值是对样本空间中所有元素它的概率与它对应的随机变量值乘积求和,因此期望值是一个随机变量的加权平均,一个随机变量的期望值为这个随机变量值的分布提供了一个中心点
        * 定义1
          * 如果$R$是定义在样本空间$S$的随机变量,那么$R$的期望就是
            * $E[R]=\sum\limits_{w\in S}R(w)P(w)$ 
        * 定理
          * 对任意的随机变量$R$ 
            * $E[R]=\sum\limits_{x\in range(R)}x\cdot P(R=x)$ 由定义1重新分组而来
        * 条件期望
          * 定义
            * 给定事件$A$的条件下,随机变量$R$的条件期望(conditional expectation)$E[R|A]$ 
              * $E[R|A]=\sum\limits_{r\in range(R)}r\cdot P(R=r|A)$ 
  * 参数估计
    * 学习意味着估计$P(Y=c_k)$和$P(X^{(j)}=x^{(j)}|Y=c_k)$ 
    * 极大似然估计
      * 先验概率$P(Y=c_k)$的极大似然估计
        * $P(Y=c_k)=\frac{\sum\limits_{i=1}^NI(y_i=c_k)}{N}$, $k=1,2,\cdots,K$ 
      * 设第$j$个特征$x^{(j)}$可能取值的集合为$\{a_{j,1},a_{j,2},\cdots,a_{j,S_j}\}$ 
        * 条件概率$P(X^{(j)}=a_{j,l}|Y=c_k)$的极大似然估计是
          * $P(X^{(j)}=a_{jl}|Y=c_k)=\frac{\sum\limits_{i=1}^NI(x^{(j)}=a_{j,l},y_i=c_k)}{\sum\limits_{i=1}^NI(y_i=c_k)}$, $j=1,2,\cdots,n$, $l=1,2,\cdots,S_j$, $k=1,2,\cdots,K$ 
      * 缺点
        * 可能会出现所要估计的概率值为0的情况,这样会影响到后验概率的计算结果,使分类产生偏差
    * 贝叶斯估计
      * 解决极大似然估计可能出现概率值为0的问题
      * 条件概率的贝叶斯估计是
        * $P_\lambda (X^{(j)}=a_{j,l}|Y=c_k)=\frac{\sum\limits_{i=1}^NI(x_i^{(j)}=a_{j,l},y_i=c_k)+\lambda}{\sum\limits_{i=1}^NI(y_i=c_k)+S_j\lambda}$, $\lambda \geq 0$ 
          * 等价于在随机变量各个取值的频率上赋予一个正数$\lambda >0$ 
          * 当$\lambda =0$时,是极大似然估计
          * 当$\lambda =1$时,是拉普拉斯平滑(Laplacian smoothing)
        * 对任何$l=1,2,\cdots,S_j$, $k=1,2,\cdots,K$有
          * $P_\lambda (X^{(j)}=a_{j,l}|Y=c_k)>0$ 
          * $\sum\limits_{l=1}^{S_j}P_\lambda (X^{(j)}=a_{j,l}|Y=c_k)=1$ 
      * 先验概率的贝叶斯估计是
        * $P_\lambda(Y=c_k)=\frac{\sum\limits_{i=1}^NI(y_i=c_k)+\lambda}{N+K\lambda}$ 

#### 朴素贝叶斯算法 (naive Bayes algorithm)

* 训练数据

  * $T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$ 
    * $x_i=(x_i^{(1)},x_i^{(2)},\cdots,x_i^{(n)})^T$, $x_i^{(j)}$是第$i$个样本的第$j$个特征
    * $x_i^{(j)}\in \{a_{j,1},a_{j,2},\cdots,a_{j,S_j}\}$, $a_{j,l}$是第$j$个特征可能取的第$l$个值
    * $j=1,2,\cdots,n$, $l=1,2,\cdots,S_j$ 
  * $y_i\in \{c_1,c_2,\cdots,c_K\}$ 

* (1) 计算先验概率即条件概率

  * $P(Y=c_k)=\frac{\sum\limits_{i=1}^NI(y_i=c_k)}{N}$
  * $P(x^{(j)}=a_{j,l}|Y=c_k)=\frac{\sum\limits_{i=1}^NI(x_i^{(j)}=a_{j,l},y_i=c_k)}{\sum\limits_{i=1}^NI(y_i=c_k)}$ 
  *  $j=1,2,\cdots,n$, $l=1,2,\cdots,S_j$, $k=1,2,\cdots,K$ 

* (2) 对给定的实例$x_i=(x_i^{(1)},x_i^{(2)},\cdots,x_i^{(n)})^T$,计算

  * $P(Y=c_k)\prod\limits_{j=1}^nP(X^{(j)}=x^{(j)}|Y=c_k)$

* (3) 确定实例$x$的分类

  * $y=arg\max\limits_{c_k}P(Y=c_k)\prod\limits_{j=1}^nP(X^{(j)}=x^{(j)}|Y=c_k)$ 

* Examples

  * 训练数据

    * ![](./训练数据.png) 

    * ```python
      import numpy as np
      from collections import Counter
      from fractions import Fraction
      X1=np.array([1]*5+[2]*5+[3]*5)
      X2=np.array(['S','M','M','S','S','S','M','M','L','L','L','M','M','L','L'])
      Y=np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])
      ```

  * 极大似然估计

    * (1) 先验概率即条件概率

      * 先验概率

        * $P(Y=1)=\frac{9}{15}$, $P(Y=-1)=\frac{6}{15}$ 

        * ```python
          Y_class_count=Counter(Y)
          Y_plus=Fraction(Y_class_count[1],len(Y))
          Y_minus=Fraction(Y_class_count[-1],len(Y))
          print(Y_plus)
          print(Y_minus)
          ```

      * 条件概率

        * $P(X^{(1)}=1|Y=1)=\frac{2}{9}$, $P(X^{(1)}=2|Y=1)=\frac{3}{9}$, $P(X^{(1)}=3|Y=1)=\frac{4}{9}$ 

        * $P(X^{(2)}=S|Y=1)=\frac{1}{9}$, $P(X^{(2)}=M|Y=1)=\frac{4}{9}$, $P(X^{(2)}=L|Y=1)=\frac{4}{9}$ 

        * $P(X^{(1)}=1|Y=-1)=\frac{3}{6}$, $P(X^{(1)}=2|Y=-1)=\frac{2}{6}$, $P(X^{(1)}=3|Y=-1)=\frac{1}{6}$ 

        * $P(X^{(2)}=S|Y=-1)=\frac{3}{6}$, $P(X^{(2)}=M|Y=-1)=\frac{2}{6}$, $P(X^{(2)}=L|Y=-1)=\frac{1}{6}$ 

        * ```python
          list_datas=[]
          for i in range(len(Y)):
              list_datas.append({'X1':X1[i],'X2':X2[i],'Y':Y[i]})
          count_Y_minus_X1_1=0
          count_Y_minus_X1_2=0
          count_Y_minus_X1_3=0
          count_Y_minus_X2_S=0
          count_Y_minus_X2_L=0
          count_Y_minus_X2_M=0
          count_Y_plus_X1_1=0
          count_Y_plus_X1_2=0
          count_Y_plus_X1_3=0
          count_Y_plus_X2_S=0
          count_Y_plus_X2_L=0
          count_Y_plus_X2_M=0
          for j in list_datas:
              if j['Y'] == -1:
                  if j['X1'] == 1:
                      count_Y_minus_X1_1+=1
                  if j['X1'] == 2:
                      count_Y_minus_X1_2+=1
                  if j['X1'] == 3:
                      count_Y_minus_X1_3+=1
                  if j['X2'] == 'S':
                      count_Y_minus_X2_S+=1
                  if j['X2'] == 'L':
                      count_Y_minus_X2_L+=1
                  if j['X2'] == 'M':
                      count_Y_minus_X2_M+=1
              if j['Y'] == 1:
                  if j['X1'] == 1:
                      count_Y_plus_X1_1+=1
                  if j['X1'] == 2:
                      count_Y_plus_X1_2+=1
                  if j['X1'] == 3:
                      count_Y_plus_X1_3+=1
                  if j['X2'] == 'S':
                      count_Y_plus_X2_S+=1
                  if j['X2'] == 'L':
                      count_Y_plus_X2_L+=1
                  if j['X2'] == 'M':
                      count_Y_plus_X2_M+=1
          ```

        * ```python
          prob_X1_1_Y_plus=Fraction(count_Y_plus_X1_1,len(X1))/Y_plus
          prob_X1_2_Y_plus=Fraction(count_Y_plus_X1_2,len(X1))/Y_plus
          prob_X1_3_Y_plus=Fraction(count_Y_plus_X1_3,len(X1))/Y_plus

          prob_X2_S_Y_plus=Fraction(count_Y_plus_X2_S,len(X2))/Y_plus
          prob_X2_M_Y_plus=Fraction(count_Y_plus_X2_M,len(X2))/Y_plus
          prob_X2_L_Y_plus=Fraction(count_Y_plus_X2_L,len(X2))/Y_plus

          prob_X1_1_Y_minus=Fraction(count_Y_minus_X1_1,len(X1))/Y_minus
          prob_X1_2_Y_minus=Fraction(count_Y_minus_X1_2,len(X1))/Y_minus
          prob_X1_3_Y_minus=Fraction(count_Y_minus_X1_3,len(X1))/Y_minus

          prob_X2_S_Y_minus=Fraction(count_Y_minus_X2_S,len(X2))/Y_minus
          prob_X2_M_Y_minus=Fraction(count_Y_minus_X2_M,len(X2))/Y_minus
          prob_X2_L_Y_minus=Fraction(count_Y_minus_X2_L,len(X2))/Y_minus
          ```

    * (2) 对给定$x=(2,S)^T$计算

      * $P(Y=1)P(X^{(1)}=2|Y=1)P(X^{(2)}=S|Y=1)=\frac{1}{45}$ 

      * ```python
        prob1=Y_plus*prob_X1_2_Y_plus*prob_X2_S_Y_plus
        ```

      * $P(Y=-1)P(X^{(1)}=2|Y=-1)P(X^{(2)}=S|Y=-1)=\frac{1}{15}$ 

      * ```
        prob2=Y_minus*prob_X1_2_Y_minus*prob_X2_S_Y_minus
        ```

    * (3) 确定实例$x$的分类

      * ```python
        OK=np.max(np.array([prob1,prob2]))
        for i in np.array([Y_minus,Y_plus]):
            y1=OK/(prob_X1_2_Y_minus*prob_X2_S_Y_minus)
            y2=OK/(prob_X1_2_Y_plus*prob_X2_S_Y_plus)
            if i == y1:
                print('-1')
            if i == y2:
                print('1')
        ```

  * 贝叶斯估计

    * $\lambda=1$拉普拉斯平滑估计概率

    * (1) 先验概率即条件概率

      - 先验概率

        - $P(Y=1)=\frac{10}{17}$, $P(Y=-1)=\frac{7}{17}$ 

        - ```python
          Y_class_count=Counter(Y)
          lam=1
          Y_bayes_plus=Fraction(Y_class_count[1]+lam,len(set(Y))*lam+len(Y))
          Y_bayes_minus=Fraction(Y_class_count[-1]+lam,len(set(Y))*lam+len(Y))
          print(Y_bayes_plus)
          print(Y_bayes_minus)
          ```

      - 条件概率

        - $P(X^{(1)}=1|Y=1)=\frac{3}{12}$, $P(X^{(1)}=2|Y=1)=\frac{4}{12}$, $P(X^{(1)}=3|Y=1)=\frac{5}{12}$ 

        - $P(X^{(2)}=S|Y=1)=\frac{2}{12}$, $P(X^{(2)}=M|Y=1)=\frac{5}{12}$, $P(X^{(2)}=L|Y=1)=\frac{5}{12}$ 

        - $P(X^{(1)}=1|Y=-1)=\frac{4}{9}$, $P(X^{(1)}=2|Y=-1)=\frac{3}{9}$, $P(X^{(1)}=3|Y=-1)=\frac{2}{9}$ 

        - $P(X^{(2)}=S|Y=-1)=\frac{4}{9}$, $P(X^{(2)}=M|Y=-1)=\frac{3}{9}$, $P(X^{(2)}=L|Y=-1)=\frac{2}{9}$ 

        - ```python
          list_datas=[]
          for i in range(len(Y)):
              list_datas.append({'X1':X1[i],'X2':X2[i],'Y':Y[i]})
          count_Y_minus_X1_1=0
          count_Y_minus_X1_2=0
          count_Y_minus_X1_3=0
          count_Y_minus_X2_S=0
          count_Y_minus_X2_L=0
          count_Y_minus_X2_M=0
          count_Y_plus_X1_1=0
          count_Y_plus_X1_2=0
          count_Y_plus_X1_3=0
          count_Y_plus_X2_S=0
          count_Y_plus_X2_L=0
          count_Y_plus_X2_M=0
          for j in list_datas:
              if j['Y'] == -1:
                  if j['X1'] == 1:
                      count_Y_minus_X1_1+=1
                  if j['X1'] == 2:
                      count_Y_minus_X1_2+=1
                  if j['X1'] == 3:
                      count_Y_minus_X1_3+=1
                  if j['X2'] == 'S':
                      count_Y_minus_X2_S+=1
                  if j['X2'] == 'L':
                      count_Y_minus_X2_L+=1
                  if j['X2'] == 'M':
                      count_Y_minus_X2_M+=1
              if j['Y'] == 1:
                  if j['X1'] == 1:
                      count_Y_plus_X1_1+=1
                  if j['X1'] == 2:
                      count_Y_plus_X1_2+=1
                  if j['X1'] == 3:
                      count_Y_plus_X1_3+=1
                  if j['X2'] == 'S':
                      count_Y_plus_X2_S+=1
                  if j['X2'] == 'L':
                      count_Y_plus_X2_L+=1
                  if j['X2'] == 'M':
                      count_Y_plus_X2_M+=1
          ```

        - ```python
          prob_X1_1_Y_plus=Fraction(count_Y_plus_X1_1+lam,len(X1))/Fraction(Y_class_count[1]+len(set(X1)),len(Y))
          prob_X1_2_Y_plus=Fraction(count_Y_plus_X1_2+lam,len(X1))/Fraction(Y_class_count[1]+len(set(X1)),len(Y))
          prob_X1_3_Y_plus=Fraction(count_Y_plus_X1_3+lam,len(X1))/Fraction(Y_class_count[1]+len(set(X1)),len(Y))

          prob_X2_S_Y_plus=Fraction(count_Y_plus_X2_S+lam,len(X2))/Fraction(Y_class_count[1]+len(set(X2)),len(Y))
          prob_X2_M_Y_plus=Fraction(count_Y_plus_X2_M+lam,len(X2))/Fraction(Y_class_count[1]+len(set(X2)),len(Y))
          prob_X2_L_Y_plus=Fraction(count_Y_plus_X2_L+lam,len(X2))/Fraction(Y_class_count[1]+len(set(X2)),len(Y))

          prob_X1_1_Y_minus=Fraction(count_Y_minus_X1_1+lam,len(X1))/Fraction(Y_class_count[-1]+len(set(X1)),len(Y))
          prob_X1_2_Y_minus=Fraction(count_Y_minus_X1_2+lam,len(X1))/Fraction(Y_class_count[-1]+len(set(X1)),len(Y))
          prob_X1_3_Y_minus=Fraction(count_Y_minus_X1_3+lam,len(X1))/Fraction(Y_class_count[-1]+len(set(X1)),len(Y))

          prob_X2_S_Y_minus=Fraction(count_Y_minus_X2_S+lam,len(X2))/Fraction(Y_class_count[-1]+len(set(X2)),len(Y))
          prob_X2_M_Y_minus=Fraction(count_Y_minus_X2_M+lam,len(X2))/Fraction(Y_class_count[-1]+len(set(X2)),len(Y))
          prob_X2_L_Y_minus=Fraction(count_Y_minus_X2_L+lam,len(X2))/Fraction(Y_class_count[-1]+len(set(X2)),len(Y))
          ```

    * (2) 对给定$x=(2,S)^T$计算

      - $P(Y=1)P(X^{(1)}=2|Y=1)P(X^{(2)}=S|Y=1)=\frac{5}{153}$ 

      - ```python
        prob1=Y_bayes_plus*prob_X1_2_Y_plus*prob_X2_S_Y_plus
        ```

      - $P(Y=-1)P(X^{(1)}=2|Y=-1)P(X^{(2)}=S|Y=-1)=\frac{28}{459}$ 

      - ```python
        prob2=Y_bayes_minus*prob_X1_2_Y_minus*prob_X2_S_Y_minus
        ```

    * (3) 确定实例$x$的分类

      * ```python
        OK=np.max(np.array([prob1,prob2]))
        for i in np.array([Y_minus,Y_plus]):
            y1=OK/(prob_X1_2_Y_minus*prob_X2_S_Y_minus)
            y2=OK/(prob_X1_2_Y_plus*prob_X2_S_Y_plus)
            if i == y1:
                print('-1')
            if i == y2:
                print('1')
        ```


