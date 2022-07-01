# 逻辑斯蒂回归与最大熵模型 (logistic regression&maximum entropy model)

* 逻辑斯蒂回归与最大熵模型都属于对数线性模型
  * 逻辑斯蒂回归 (logistic regression)是统计学习中的分类方法
  * 最大熵模型 (maximum entropy model)是统计学习中的分类方法
    * 最大熵是概率模型学习的一个准则

#### 逻辑斯蒂回归模型

* 逻辑斯蒂分布 (logistic distribution)

  * 定义
    * 设$X$是连续随机变量,$X$服从逻辑斯蒂分布是指$X$具有以下
      * 分布函数
        * $F(x)=P(X\leq x)=\frac{1}{1+e^{-(x-\mu)/\gamma}}$ 
      * 密度函数
        * $f(x)=F'(x)=\frac{e^{-(x-\mu)/\gamma}}{\gamma(1+e^{-(x-\mu)/\gamma})^2}$ 
      * $\mu$为位置参数
      * $\gamma>0$为形状参数

* 二项逻辑斯蒂回归模型(binomial logistic regression model)

  * 由条件概率分布$P(Y|X)$表示,形式为参数化的逻辑斯蒂分布

    * 随机变量$X$取值为实数,随机变量$Y$取值为1或0

  * 定义

    * 二项逻辑斯蒂回归模型是如下的条件概率分布
      * $P(Y=1|x)=\frac{\exp(w\cdot x+b)}{1+\exp(w\cdot x+b)}$ 
      * $P(Y=0|x)=\frac{1}{1+\exp(w\cdot x+b)}$ 
      * $w\cdot x$为$w$和$x$的内积
      * 输入
        * $x\in R^n$
      * 输出
        * $Y\in\{0,1\}$ 
      * 参数
        * $w\in R^n$, 权值向量
        * $b\in R$, **偏置**

  * 对于给定的输入实例$x$, 可以求得$P(Y=1|x)$, $P(Y=0|x)$, 比较两个条件概率值的大小,将实例$x$分到概率值较大的那一类

  * 为了方便,将权值向量和输入向量加以扩充

    * 仍记作$w$, $x$
      * $w=(w^{(1)},w^{(2)},\cdots,w^{(n)},b)^T$ 
      * $x=(x^{(1)},x^{(2)},\cdots,x^{(n)},1)^T$ 
    * $P(Y=1|x)=\frac{\exp(w\cdot x)}{1+\exp(w\cdot x)}$ 
    * $P(Y=0|x)=\frac{1}{1+\exp(w\cdot x)}$ 

  * 几率 (odds)

    * 一个事件的几率是指该事件发生的概率与该事件不发生的概率的比值
      * 如,事件发生的概率为$p$, 事件不发生的概率为$1-p$, 那么事件的几率为
        * $\frac{p}{1-p}$ 
    * 对数几率 (log odds)
      * logit函数
        * $logit(p)=\log \frac{p}{1-p}$ 

  * 逻辑斯蒂的对数几率

    * $\log\frac{P(Y=1|x)}{1-P(Y=1|x)}=w\cdot x$ 
    * 在逻辑斯蒂回归模型中, 输入$Y=1$的对数几率是输入$x$的线性函数
    * 输入$Y=1$的对数几率是输入$x$的线性函数表示的模型,即逻辑斯蒂回归模型

  * 通过逻辑斯蒂回归模型将线性函数$w\cdot x$转换为概率

    * $P(Y=1|x)=\frac{\exp(w\cdot x)}{1+\exp(w\cdot x)}$ 

    * 线性函数的值越接近正无穷,概率值就越接近1

    * 线性函数的值越接近负无穷,概率值就越接近0

    * ```python
      import numpy as np
      f=lambda x:np.exp(x)/(1+np.exp(x))
      display(f(5),f(-5))
      ```

* 模型参数估计

  * 应用极大似然估计法估计模型参数,得到逻辑斯蒂回归模型
    * 设
      * $P(Y=1|x)=\pi(x)$, $P(Y=0|x)=1-\pi(x)$ 
    * 似然函数为
      * $\prod\limits_{i=1}^N[\pi(x_i)]^{y_i}[1-\pi(x_i)]^{1-y_i}$ 
    * 对数似然函数为
      * $L(w)=\sum\limits_{i=1}^N[y_i\log \pi(x_i)+(1-y_i)\log(1-\pi(x_i))]$ 
      * ​           $=\sum\limits_{i=1}^N[y_i\log\frac{\pi(x_i)}{1-\pi(x_i)}+\log(1-\pi(x_i))]$ 
      * ​           $=\sum\limits_{i=1}^N[y_i(w\cdot x)-\log(1+\exp(w\cdot x))]$ 
  * 对$L(w)$求极大值,得到$w$的估计值
    * 这样问题就变成了以对数似然函数为目标函数的最优化问题
    * 设$w$的极大似然估计值是$\hat{w}$,那么学到的逻辑斯蒂回归模型为
      * $P(Y=1|x)=\frac{\exp(\hat{w}\cdot x)}{1+\exp(\hat{w}\cdot x)}$ 
      * $P(Y=0|x)=\frac{1}{1+\exp(\hat{w}\cdot x)}$ 

* 多项逻辑斯蒂回归模型 (multi-nominal logistic regression model)

  * 设
    * 离散型随机变量$Y$的取值集合是
      * $\{1,2,\cdots,K\}$ 
  * 多项逻辑斯蒂回归模型
    * $P(Y=k|x)=\frac{\exp(w_k\cdot x)}{1+\sum\limits_{k=1}^{K-1}\exp(w_k\cdot x)}$ 
      * $k=1,2,\cdots,K-1$ 
    * $P(Y=K|x)=\frac{1}{1+\sum\limits_{k=1}^{K-1}\exp(w_k\cdot x)}$ 
    * $x\in R^{n+1}$, $w_k\in R^{n+1}$ 
  * 模型参数估计
    - 应用极大似然估计法估计模型参数,得到逻辑斯蒂回归模型
      - 设
        - $P(Y=k|x)=\pi(x)$, $P(Y=K|x)=1-\pi(x)$ 
      - 似然函数为
        - $\prod\limits_{i=1}^N[\pi(x_i)]^{y_k}[1-\pi(x_i)]^{1-y_K}$ 
      - 对数似然函数为
        - $L(w)=\sum\limits_{i=1}^N[y_k\log \pi(x_i)+(1-y_K)\log(1-\pi(x_i))]$ 
        - ​           $=\sum\limits_{i=1}^N[y_k\log\frac{\pi(x_i)}{1-\pi(x_i)}+\log(1-\pi(x_i))]$ 
        - ​           $=\sum\limits_{i=1}^N[y_i(w_k\cdot x)-\log(1+\exp(w_k\cdot x))]$ 
    - 对$L(w)$求极大值,得到$w$的估计值
      - 这样问题就变成了以对数似然函数为目标函数的最优化问题
      - 设$w$的极大似然估计值是$\hat{w}$,那么学到的逻辑斯蒂回归模型为
        - $P(Y=k|x)=\frac{\exp(\hat{w_k}\cdot x)}{1+\exp(\hat{w_k}\cdot x)}$ 
        - $P(Y=K|x)=\frac{1}{1+\exp(\hat{w_k}\cdot x)}$ 

#### 最大熵模型

* 最大熵原理
  * 最大熵原理是概率模型学习的一个准则
  * 最大熵原理认为,学习概率模型时,在所有可能的概率模型(分布)中,熵最大的模型是最好的模型
  * 通常用约束条件来确定概率模型的集合,最大熵原理也可以表述为在满足约束条件的模型集合中选取熵最大的模型
  * 最大熵原理认为要选择的概率模型首先必须满足已有的事实,即约束条件
  * 在没有更多信息的情况下,那些不确定的部分都是"等可能的"
  * 最大熵原理通过熵的最大化来表示等可能性
  * "等可能"不容易操作,而熵则是一个可优化的数值指标
* 最大熵模型的定义
  * 假设
    * 分类模型是一个条件概率分布$P(Y|X)$ 
      * $X\in \cal X \rm \subseteq R^n$, 表示输入
      * $Y\in \cal Y$, 表示输出
        * $\cal X, Y$分别表示输入输出的集合
  * 这个模型表示的是对于给定的输入$X$,以条件概率$P(Y|X)$输出$Y$
  * 给定一个训练数据集
    * $T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$ 
  * 联合分布$P(X,Y)$的经验分布
    * $\widetilde{P}(X=x,Y=y)=\frac{v(X=x,Y=y)}{N}$ 
    * $v(X=x,Y=y)$表示训练数据中样本$(x,y)$出现的频数, $N$表示训练样本容量
  * 边缘分布$P(X)$的经验分布
    * $\widetilde{P}(X=x)=\frac{v(X=x)}{N}$ 
    * $v(X=x)$表示训练数据中输入$x$出现的频数, $N$表示训练样本容量
  * 特征函数 (feature function)
    * $f(x,y)=\begin{cases}1,x与y满足某一事实\\0,否则\end{cases}$ 
    * $f(x,y)$ (是一个二值函数)描述输入$x$和输出$y$之间的某一个事实
      * 当$x$和$y$满足这个事实时取值为1
      * 否则取值为0
  * 特征函数$f(x,y)$关于经验分布$\widetilde{P}(X,Y)$的期望值
    * $E_{\widetilde{P}}(f)=\sum\limits_{x,y}\widetilde{P}(x,y)f(x,y)$ 
  * 特征函数$f(x,y)$关于模型$P(Y|X)$与经验分布$\widetilde{P}(X)$的期望值
    * $E_P(f)=\sum\limits_{x,y}\widetilde{P}(x)P(y|x)f(x,y)$ 
  * 如果模型能够获取训练数据中的信息,那么就可以假设这两个期望值相等
    * $E_{\widetilde{P}}(f)=E_P(f)$ 
  * 将$E_{\widetilde{P}}(f)=E_P(f)$作为模型学习的约束条件
    * 假设有$n$个特征函数$f_i(x,y)$, 那么就有$n$个约束条件, $i=1,2,\cdots,n$ 
  * 定义
    * 假设满足所有约束条件的模型集合为
      * $\cal C\rm \equiv\{P\in \cal P\it |E_P(f_i)=E_{\widetilde{P}}(f_i)\}$, $i=1,2,\cdots,n$ 
      * $\cal P$概率模型集合
    * 定义在条件概率分布$P(Y|X)$上的条件熵为
      * $H(P)=-\sum\limits_{x,y}\widetilde{P}(x)P(y|x)\log P(y|x)$ 
    * 模型集合$\cal C$中条件熵$H(P)$最大的模型称为最大熵模型
* **拉格朗日乘子**
  * **拉格朗日乘子法,求解有约束多变量最优化问题**
  * 给定一个函数
    * $y=f(x_1,\cdots,x_n)$ 
  * 给定一组约束(假设这些约束可以用$k$个等式表示)
    * $\begin{matrix}g_1(x_1,\cdots,x_n)=c_1\\g_2(x_1,\cdots,x_n)=c_2\\\vdots\\g_k(x_1,\cdots,x_n)=c_k\end{matrix}$ 
  * 目标
    * 在集合$S=\{(x_1,\cdots,x_n):g_i(x_1,\cdots,x_n)=c_i\}$, $i=1,\cdots,k$上
    * 对$y=f(x_1,\cdots,x_n)$求最大值
    * 一个定理保证了在极值点$x\in S$, 一定有
      * $\nabla f=\lambda_1\nabla g_1+\cdots+\lambda_k\nabla g_k$ 
        * $\lambda_1,\cdots,\lambda_k$称为拉格朗日乘子
  * 假设$\nabla g_1,\cdots,\nabla g_k$是线性无关向量
  * 为了求出$f$在集合$S$上的极大值或极小值点
    * 求解关于变量$x_1,\cdots,x_n$和$\lambda_1,\cdots,\lambda_k$的$n$个拉格朗日乘子方程
      * $\begin{matrix}\frac{\partial f}{\partial x_1}=\lambda_1\frac{\partial g_1}{\partial x_1}+\cdots+\lambda_k\frac{\partial g_k}{\partial x_1}\\\vdots\\\frac{\partial f}{\partial x_n}=\lambda_1\frac{\partial g_1}{\partial x_n}+\cdots+\lambda_k\frac{\partial g_k}{\partial x_n}\end{matrix}$ 
    * 及$k$个约束方程
      * $\begin{matrix}g_1(x_1,\cdots,x_n)=c_1\\g_2(x_1,\cdots,x_n)=c_2\\\vdots\\g_k(x_1,\cdots,x_n)=c_k\end{matrix}$ 
    * 还要检查那些不满足梯度向量$\nabla g_1,\cdots,\nabla g_k$线性无关的异常点
  * 拉格朗日乘子法以梯度向量的几何解释为基础
    * 假设只有**一个约束**函数
      * $g(x_1,\cdots,x_n)=c$ 
    * 则拉格朗日乘子方程变为
      * $\nabla f=\lambda \nabla g$ 
      * 线性无关,即
        * $\nabla g\not=0$ 
    * 集合$g=c$为$R^n$中的$n-1$维曲面
      * 对任意点$x\in S$, 梯度向量$\nabla g(x)$在这点与$S$垂直
      * 而梯度向量$\nabla f$总是指向$f$增加最快的方向
    * 在局部的极大或极小值点, $f$增加最快的方向也应该与$S$垂直
      * 于是在这一点,$\nabla f$与$\nabla g$指向同一个方向,即
        * $\nabla f=\lambda \nabla g$ 
    * **多约束**的情况下,几何的原理是类似的
      * 现在$S$为$k$个曲面$g_1=c_1\cdots,g_k=c_k$的交集
        * 每个曲面都是$R^n$中的$n-1$维子集
        * 从而它们的交集为$n-k$维子集
      * 在极值点
        * $\nabla f$一定与$S$垂直
          * 因为它一定**在**由$k$个向量$\nabla g_1,\cdots,\nabla g_k$张成的线性空间中
      * 线性无关的假设保证了这$k$个向量$\nabla g_1,\cdots,\nabla g_k$可以生成一个$k$维线性空间
* **拉格朗日对偶性** (Lagrange duality)
  * 策略
    * 约束优化问题中,利用拉格朗日对偶性将原始问题转换为对偶问题,通过解对偶问题而得到原始问题的解
  * ***原始问题***
    * 假设$f(x),c_i(x),h_i(x)$是定义在$R^n$上的连续可微函数
      * $\min\limits_{x\in R^n}\ f(x)$
      * $s.t.\ \ c_i(x)\leq0$, $i=1,2,\cdots,k$
      * ​          $h_j(x)=0$, $j=1,2,\cdots,l$ 
      * 考虑约束最优化问题,称此约束最优化问题为原始最优化问题或原始问题
    * 广义拉格朗日函数 (generalized Lagrange function)
      * $L(x,\alpha,\beta)=f(x)+\sum\limits_{i=1}^k\alpha_ic_i(x)+\sum\limits_{j=1}^l\beta_jh_j(x)$ 
        * $x=(x^{(1)},x^{(2)},\cdots,x^{(n)})^T\in R^n$, $\alpha_i,\beta_i$是拉格朗日乘子,$\alpha_i\geq0$ 
      * 考虑$x$的函数
        * $\theta_P(x)=\max\limits_{\alpha,\beta:\alpha_i\geq0}L(x,\alpha,\beta)$ 
          * 下标$P$表示原始问题
    * 假设给定某个$x$,如果$x$违反原始问题的约束条件
      * 即存在某个$i$使得$c_i(x)>0$
      * 或者存在某个$j$使得$h_j(x)\not=0$ 
      * $\theta_P(x)=\max\limits_{\alpha,\beta:\alpha_i\geq0}[f(x)+\sum\limits_{i=1}^k\alpha_ic_i(x)+\sum\limits_{j=1}^l\beta_jh_j(x)]=+\infty$ 
        * 因为若某个$i$使约束$c_i(x)>0$, 则可令$\alpha_i\rightarrow +\infty$
        * 若某个$j$使$h_j(x)\not=0$, 则可令$\beta_j$使$\beta_jh_j(x)\rightarrow +\infty$
        * 而将其余$\alpha_i,\beta_j$均取为0
    * 如果$x$满足约束条件$c_i(x)\leq0$, $h_j(x)=0$ 
      * 则由式$\theta_P(x)=\max\limits_{\alpha,\beta:\alpha_i\geq0}L(x,\alpha,\beta)$ 和式$L(x,\alpha,\beta)=f(x)+\sum\limits_{i=1}^k\alpha_ic_i(x)+\sum\limits_{j=1}^l\beta_jh_j(x)$ 
      * 可知$\theta_P(x)=f(x)$ 
    * $\theta_P(x)=\begin{cases}f(x),&x满足原始问题约束\\+\infty,&其他\end{cases}$ 
      * 如果考虑极小化问题
        * $\min\limits_{x}\theta_P(x)=\min\limits_x\max\limits_{\alpha,\beta:\alpha_i\geq0}L(x,\alpha,\beta)$ 
        * 它是与原始最优化问题等价的,即它们有相同的解
        * 问题$\min\limits_x\ \max\limits_{\alpha,\beta:\alpha_i\geq0}L(x,\alpha,\beta)$称为广义拉格朗日函数的极小极大问题
        * 把原始最优化问题表示为广义拉格朗日函数的极小极大问题
    * 定义原始问题的最优值,称为原始问题的值
      * $p^*=\min\limits_x\theta_P(x)$ 
  * ***对偶问题***
    * 定义
      * $\theta_D(\alpha,\beta)=\min\limits_xL(x,\alpha,\beta)$ 
    * 考虑极大化$\theta_D(\alpha,\beta)$ 
      * $\max\limits_{\alpha,\beta:\alpha_i\geq0}\theta_D(\alpha,\beta)=\max\limits_{\alpha,\beta:\alpha_i\geq0}\min\limits_xL(x,\alpha,\beta)$ 
    * $\max\limits_{\alpha,\beta:\alpha_i\geq0}\min\limits_xL(x,\alpha,\beta)$称为广义拉格朗日函数的极大极小问题
    * 可以将广义格朗日函数的极大极小问题表示为约束最优化问题,称为原始问题的对偶问题
      * $\max\limits_{\alpha,\beta}\theta_D(\alpha,\beta)=\max\limits_{\alpha,\beta}\min\limits_xL(x,\alpha,\beta)$ 
      * $s.t.\ \alpha_i\geq0$, $i=1,2,\cdots,k$ 
    * 定义对偶问题的最优值,称为对偶问题的值
      * $d^*=\max\limits_{\alpha,\beta:\alpha_i\geq0}\theta_D(\alpha,\beta)$ 
  * ***原始问题和对偶问题的关系***
    * 定理1
      * 若原始问题和对偶问题都有最优值
        * $d^*=\max\limits_{\alpha,\beta:\alpha_i\geq0}\min\limits_xL(x,\alpha,\beta)\leq\min\limits_x\max\limits_{\alpha,\beta:\alpha_i\geq0}L(x,\alpha,\beta)=p^*$ 
      * 证明
        * 由$\max\limits_{\alpha,\beta}\theta_D(\alpha,\beta)=\max\limits_{\alpha,\beta}\min\limits_xL(x,\alpha,\beta)$与$\theta_P(x)=\max\limits_{\alpha,\beta:\alpha_i\geq0}L(x,\alpha,\beta)$ 
        * 对任意的$\alpha,\beta,x$有
          * $\theta_D(\alpha,\beta)=\min\limits_xL(x,\alpha,\beta)\leq L(x,\alpha,\beta)\leq \max\limits_{\alpha,\beta:\alpha_i\geq0}L(x,\alpha,\beta)=\theta_P(x)$ 
        * 即
          * $\theta_D(\alpha,\beta)\leq \theta_P(x)$
        * 由于原始问题和对偶问题均有最优值,所以
          * $\max\limits_{\alpha,\beta:\alpha_i\geq0}\theta_D(\alpha,\beta)\leq\min\limits_x\theta_P(x)$
          * 即
            * $d^*=\max\limits_{\alpha,\beta:\alpha_i\geq0}\min\limits_xL(x,\alpha,\beta)\leq\min\limits_x\max\limits_{\alpha,\beta:\alpha_i\geq0}L(x,\alpha,\beta)=p^*$ 
    * 推论1
      * 设
        * $x^*$是原始问题的可行解
        * $\alpha^*,\beta^*$是对偶问题的可行解
      * 并且$d^*=p^*$,
      * 则
        * $x^*$是原始问题的最优解
        * $\alpha^*,\beta^*$是对偶问题的最优解
    * 在某些条件下,原始问题和对偶问题的最优值相等, $d^*=p^*$, 这时可以**用解对偶问题替代解原始问题**
      * 定理2
        * 考虑原始问题和对偶问题
        * 假设函数$f(x)$和$c_i(x)$是凸函数, $h_j(x)$是仿射函数;并且假设不等式约束$c_i(x)$是严格可行的
          * 即存在$x$对所有$i$有$c_i(x)<0$,则存在$x^*,\alpha^*,\beta^*$ 
            * 使$x^*$是原始问题的解
            * $\alpha^*,\beta^*$是对偶问题的解
          * 并且
            * $p^*=d^*=L(x^*,\alpha^*,\beta^*)$ 
      * 定理3
        * 对原始问题和对偶问题
        * 假设函数$f(x)$和$c_i(x)$是凸函数, $h_j(x)$是仿射函数,并且不等式约束$c_i(x)$是严格可行的
          * 则$x^*$和$\alpha^*,\beta^*$分别是原始问题和对偶问题的解的充分必要条件是
          * $x^*,\alpha^*,\beta^*$满足下面KKT(Karush-Kuhn-Tucker)条件
            * $\nabla_xL(x^*,\alpha^*,\beta^*)=0$
            * $\alpha_i^*c_i(x^*)=0$,      $i=1,2,\cdots,k$ 
              * 称为KKT的对偶互补条件
                * 若$\alpha_i^*>0$
                * 则$c_i(x^*)=0$ 
            * $c_i(x^*)\leq0$,           $i=1,2,\cdots,k$ 
            * $\alpha_i^*\geq0$,                 $i=1,2,\cdots,k$ 
            * $h_j(x^*)=0$,         $j=1,2,\cdots,l$ 
  * KKT
    * <img src="./imgs/KKT.png" style="zoom:30%;" /> 
* 最大熵模型的学习
  * 最大熵模型的学习过程就是求解最大熵模型的过程
  * 最大熵模型的学习可以形式化为约束最优化问题
  * 给定
    - 训练数据集
      - $T=\{(x_1,y_1),(x_2,y_2),\cdots,(x_N,y_N)\}$ 
    - 特征函数
      - $f_i(x,y)$, $i=1,2,\cdots,n$ 
    - 最大熵模型的学习等价于约束最优化问题
      - $\max\limits_{P\in C}$  $H(P)=-\sum\limits_{x,y}\widetilde{P}(x)P(y|x)\log P(y|x)$ 
      - $s.t.$   $E_P(f_i)=E_{\widetilde{P}}(f_i)$ 
      - ​          $\sum\limits_yP(y|x)=1$ 
    - 将求最大值问题改写为等价的求最小值问题
      - $\min\limits_{P\in C}$  $-H(P)=\sum\limits_{x,y}\widetilde{P}(x)P(y|x)\log P(y|x)$ 
      - $s.t.$   $E_P(f_i)-E_{\widetilde{P}}(f_i)=0$ 
      - ​          $\sum\limits_yP(y|x)=1$ 
    - 求解约束最优化问题,所得出的解,就是最大熵模型学习的解
  * 具体推导过程
    * 策略
      * 将约束最优化的原始问题转换为无约束最优化的对偶问题,通过求解对偶问题求解原始问题
    * 引进拉格朗日乘子$w_0,w_1,w_2,\cdots,w_n$,定义拉格朗日函数$L(P,w)$
      * $L(P,w)\equiv -H(P)+w_0(1-\sum\limits_yP(y|x))+\sum\limits_{i=1}^nw_i(E_{\widetilde{P}}(f_i)-E_P(f_i))$ 
      * ​                $=\sum\limits_{x,y}\widetilde{P}(x)P(y|x)\log P(y|x)+w_0(1-\sum\limits_yP(y|x))+\sum\limits_{i=1}^nw_i(\sum\limits_{x,y}\widetilde{P}(x,y)f(x,y)-\sum\limits_{x,y}\widetilde{P}(x)P(y|x)f(x,y))$ 
    * 最优化原始问题
      * $\min\limits_{P\in C}$ $\max\limits_wL(P,w)$ 
    * 对偶问题是
      * $\max\limits_w$ $\min\limits_{P\in C}L(P,w)$
    * 由于拉格朗日函数$L(P,w)$是$P$的凸函数
      * 原始问题的解与对偶问题的解是等价的
    * 首先,求解对偶问题内部的极小化问题$\min\limits_{P\in C}L(P,w)$ 
      * $\min\limits_{P\in C}L(P,w)$是$w$的函数,将其记作
        * $\Psi(w)=\min\limits_{P\in C}L(P,w)=L(P_w,w)$ 
      * $\Psi$称为对偶函数,将其解记作
        * $P_w=arg\min\limits_{P\in C}L(P,w)=P_w(y|x)$ 
      * 求$L(P,w)$对$P(y|x)$的偏导数
        * $\frac{\partial L(P,w)}{\partial P(y|x)}=\sum\limits_{x,y}\widetilde{p}(x)(\log P(y|x)+1)-\sum\limits_yw_0-\sum\limits_{x,y}(\widetilde{P}(x)\sum\limits_{i=1}^nw_if_i(x,y))$ 
        * ​              $=\sum\limits_{x,y}\widetilde{P}(x)(\log P(y|x)+1-w_0-\sum\limits_{i=1}^nw_if_i(x,y))$ 
      * 令偏导数等于0,在$\widetilde{P}(x)>0$的情况下,解得
        * $P(y|x)=\exp(\sum\limits_{i=1}^nw_if_i(x,y)+w_0-1)$ 
        * ​              $=\frac{\exp(\sum\limits_{i=1}^nw_if_i(x,y))}{\exp(1-w_0)}$ 
      * 由$\sum\limits_yP(y|x)=1$, 得
        * $P_w(y|x)=\frac{\exp(\sum\limits_{i=1}^nw_if_i(x,y))}{Z_w(x)}$ 
          * $Z_w(x)=\sum\limits_y\exp(\sum\limits_{i=1}^nw_if_i(x,y))$, 规范化因子
          * $f_i(x,y)$是特征函数
          * $w_i$是特征的权值
      * $P_w=P_w(y|x)$就是最大熵模型, $w$是最大熵模型中的参数向量
    * 然后,求解对偶问题外部的极大化问题
      * $\max\limits_w\Psi(w)$ 
      * 将其记为
        * $w^*=arg\max\limits_w\Psi(w)$ 
      * 可以应用最优化算法求对偶函数$\Psi(w)$的极大化,得到$w^*$,用来表示$P^*\in \cal C$
        * $P^*=P_{w^*}=P_{w^*}(y|x)$是学习到的最优模型(最大熵模型)
          * 也就是说,最大熵模型的学习归结为对偶函数$\Psi(w)$的极大化
* 极大似然估计
  * 证明对偶函数的极大化等价于最大熵模型的极大似然估计
  * 已知训练数据的经验概率分布$\widetilde{P}(X,Y)$, 条件概率分布$P(Y|X)$, 的对数似然函数表示为
    * $L_{\widetilde{P}}(P_w)=\log\prod\limits_{x,y}P(y|x)^{\widetilde{P}(x,y)}=\sum\limits_{x,y}\widetilde{P}(x,y)\log P(y|x)$ 
  * 当条件概率分布$P(y|x)$是最大熵模型
    * $P_w(y|x)=\frac{1}{Z_w(x)}\exp(\sum\limits_{i=1}^nw_if_i(x,y))$, 时
      * $Z_w(x)=\sum\limits_y\exp(\sum\limits_{i=1}^nw_if_i(x,y))$ 
    * 对数似然函数$L_{\widetilde{P}}(P_w)$为
      * $L_{\widetilde{P}}(P_w)=\sum\limits_{x,y}\widetilde{P}(x,y)\log P(y|x)$ 
      * ​                $=\sum\limits_{x,y}\widetilde{P}(x,y)\sum\limits_{i=1}^nw_if_i(x,y)-\sum\limits_{x,y}\widetilde{P}(x,y)\log Z_w(x)$ 
      * ​                $=\sum\limits_{x,y}\widetilde{P}(x,y)\sum\limits_{i=1}^nw_if_i(x,y)-\sum\limits_{x}\widetilde{P}(x)\log Z_w(x)$ 
  * 由
    * $L(P,w)\equiv -H(P)+w_0(1-\sum\limits_yP(y|x))+\sum\limits_{i=1}^nw_i(E_{\widetilde{P}}(f_i)-E_P(f_i))$
      * $=\sum\limits_{x,y}\widetilde{P}(x)P(y|x)\log P(y|x)+w_0(1-\sum\limits_yP(y|x))+\sum\limits_{i=1}^nw_i(\sum\limits_{x,y}\widetilde{P}(x,y)f(x,y)-\sum\limits_{x,y}\widetilde{P}(x)P(y|x)f(x,y))$
    * $\Psi(w)=\min\limits_{P\in C}L(P,w)=L(P_w,w)$ 
    * 对偶函数$\Psi(w)$可得
      * $\Psi(w)=\sum\limits_{x,y}\widetilde{P}(x)P(y|x)\log P(y|x)+\sum\limits_{i=1}^nw_i(\sum\limits_{x,y}\widetilde{P}(x,y)f(x,y)-\sum\limits_{x,y}\widetilde{P}(x)P(y|x)f(x,y))$ 
        * ​    $=\sum\limits_{x,y}\widetilde{P}(x,y)\sum\limits_{i=1}^nw_if_i(x,y)+\sum\limits_{x,y}\widetilde{P}(x)P_w(y|x)(\log P_w(y|x)-\sum\limits_{i=1}^nw_if_i(x,y))$ 
        * ​    $=\sum\limits_{x,y}\widetilde{P}(x,y)\sum\limits_{i=1}^nw_if_i(x,y)-\sum\limits_{x,y}\widetilde{P}(x)P_w(y|x)\log Z_w(x)$ 
        * ​    $=\sum\limits_{x,y}\widetilde{P}(x,y)\sum\limits_{i=1}^nw_if_i(x,y)-\sum\limits_{x}\widetilde{P}(x)\log Z_w(x)$ 
  * 比较
    * 对数似然函数$L_{\widetilde{P}}(P_w)$ 
    * 对偶函数$\Psi(w)$ 
  * 可得
    * $\Psi(w)=L_{\widetilde{P}}(P_w)$ 
    * 证明了最大熵模型学习中得对偶函数极大化等价于最大熵模型的极大似然估计
  * 最大熵学习问题转换为具体求解对数似然函数极大化或对偶函数极大化问题
    * 可以将最大熵模型写成更一般的形式
      * $P_w(y|x)=\frac{1}{Z_w(x)}\exp(\sum\limits_{i=1}^nw_if_i(x,y))$
        * $Z_w(x)=\sum\limits_y\exp(\sum\limits_{i=1}^nw_if_i(x,y))$ 
        * $x\in R^n$为输入
        * $y\in \{1,2,\cdots,K\}$为输出
        * $w\in R^n$为权值向量
        * $f_i(x,y)$为任意实值特征向量 $i=1,2,\cdots,n$ 

#### 总结

* 最大熵模型与逻辑斯蒂回归模型有类似的形式,它们又称为对数线性模型(log linear model)
* 模型学习就是在给定的训练数据条件下对模型进行极大似然估计或正则化的极大似然估计
