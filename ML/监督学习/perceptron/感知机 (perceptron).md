# 感知机 (perceptron)

* Rosenblatt

  * 于1957年提出

* **Abstract**

  * 感知机是二类分类的线性分类模型,其输入为实例的特征向量,输出为实例的类别
  * 感知机对应于输入空间中将实例划分为正负两类的分离超平面,属于**判别模型**

* #### 感知机模型

  * 定义
    * 假设
      * 输入空间(特征空间)是$\cal{X}\sube \rm R^n$ 
        * 输入$x\in\cal X$表示实例的特征向量,对应于输入空间(特征空间)的点
      * 输出空间是$\cal Y=\rm\{+1,-1\}$ 
        * 输出$y\in\cal Y$表示实例的类别
    * 由输入空间到输出空间的函数称为感知机
      * $f(x)=sign(w\cdot x+b)$ 
        * $w,b$为感知机模型参数
          * $w\in R^n$叫作权值(weight)或权值向量(weight vector)
          * $b\in R$叫做偏置(bias)
          * $w\cdot x$表示$w$和$x$的内积
          * $sign$是符号函数
            * $sign(x)=\begin{cases}+1,&x\geq0\\-1,&x<0\end{cases}$ 
  * 感知机模型的假设空间是定义在特征空间中的所有线性分类模型(linear classification model)或线性分类器(linear classifier)
    * $\{f|f(x)=w\cdot x+b\}$ 

#### 感知机学习策略

* 