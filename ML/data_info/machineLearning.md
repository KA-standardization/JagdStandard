$$\theta$$为权重

$$x$$为特征值 $$x_1,x_2$$为特征

$$h_\theta(x)$$为预测值也就是$$y$$_
$$
h_\theta(x) = \theta_0+\theta_1x_1+\theta_2x_2
$$

$$
h_\theta(x)=\sum_{i=0}^n\theta_ix_i=\theta^Tx
$$

$$y^{(i)}$$为真实值

$$\varepsilon^{(i)}$$为误差值  独立并且具有相同的分布(独立同分布),通常认为服从均值为0方差为$$\theta^2$$的高斯分布
$$
y^{(i)}=\theta^Tx^{(i)}+\varepsilon^{(i)}
$$

$$
P(\varepsilon^{(i)})=\frac{1}{\sqrt{2\pi}\sigma}exp(-\frac{(\epsilon^{(i)})^2}{2\sigma^2})
$$

$$P(y^{(i)}|x^{(i)};\theta)$$什么样的$$\theta$$和$$x^{(i)}$$组合后越接近$$y^{(i)}$$的概率值越大的
$$
P(y^{(i)}|x^{(i)};\theta)=\frac{1}{\sqrt{2\pi}\sigma}exp(-\frac{(y^{(i)}-\theta^Tx^{(i)})^2}{2\sigma^2})
$$
$$L(\theta)$$似然函数 越大模型越好
$$
L(\theta)=\prod_{i=1}^mP(y^{(i)}|x^{(i)};\theta)
$$

$$
L(\theta)=\prod_{i=1}^m\frac{1}{\sqrt{2\pi}\sigma}exp(-\frac{(y^{(i)}-\theta^Tx^{(i)})^2}{2\sigma^2})
$$

$$
\lg L(\theta)=\lg \prod_{i=1}^m\frac{1}{\sqrt{2\pi}\sigma}exp(-\frac{(y^{(i)}-\theta^Tx^{(i)})^2}{2\sigma^2})
$$

$$\lg AB=\lg A+\lg B$$
$$
=\sum_{i=1}^m\lg \frac{1}{\sqrt{2\pi}\sigma}exp(-\frac{(y^{(i)}-\theta^Tx^{(i)})^2}{2\sigma^2})
$$

$$
=m\lg \frac{1}{\sqrt{2\pi}\sigma}-\frac{1}{\sigma^2}\frac{1}{2}\sum_{i=1}^m(y^{(i)}-\theta^Tx^{(i)})^2
$$

$J(\theta)$越小越好
$$
J(\theta)=\frac{1}{2}\sum_{i=1}^m(h_\theta(x^{(i)}-y^{(i)})^2
$$

$$
=\frac{1}{2}(X\theta-y)^T(X\theta-y)
$$

矩阵的平方等于自身的转置乘以自身
$$
\nabla J(\theta)=\nabla_\theta \{\frac{1}{2}(X\theta-y)^T(X\theta-y)\}
$$

$$
=\nabla_\theta \{\frac{1}{2}(\theta^TX^T-y^T)(X\theta-y)\}
$$

$$
=\nabla_\theta \{\frac{1}{2}(\theta^TX^TX\theta-\theta^TX^Ty-y^TX\theta+y^Ty)\}
$$

$$
=\frac{1}{2}(2X^TX\theta-X^Ty-(y^TX)^T)
$$

$$
0=X^TX\theta-X^Ty
$$

极值点 导数等于0
$$
\theta=(X^TX)^{-1}X^Ty
$$
Sigmoid函数
$$
g(z)=\frac{1}{1+e^{-z}}
$$

$$
h_\theta(x)=g(\theta^Tx)=\frac{1}{1+e^{-\theta^Tx}}
$$

$$
g'(x)=\frac{e^{-x}}{(1+e^{-x})^2}
$$

$$
=\frac{1}{1+e^{-x}}\frac{e^{-x}}{1+e^{-x}}
$$

$$
=\frac{1}{1+e^{-x}}(1-\frac{1}{1+e^{-x}})
$$

$$
=g(x)(1-g(x))
$$

