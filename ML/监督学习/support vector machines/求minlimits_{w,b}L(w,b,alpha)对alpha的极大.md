求$\min\limits_{w,b}L(w,b,\alpha)$对$\alpha$的极大

​	$\max\limits_\alpha\ -\frac{1}{2}\sum\limits_{i=1}^N\sum\limits_{j=1}^N\alpha_{i}\alpha_{j}y_iy_j(x_i\cdot x_j)+\sum\limits_{i=1}^N\alpha_{i}$ 

​	$s.t.$   $\sum\limits_{i=1}^N\alpha_iy_i=0$ 

​				$\alpha_i\geq 0, i=1,2,\cdots,N$ 

对偶问题,目标函数由求极大转换成求极小,

得到等价的对偶最优化问题

​		$\min\limits_\alpha\ \frac{1}{2}\sum\limits_{i=1}^N\sum\limits_{j=1}^N\alpha_{i}\alpha_{j}y_iy_j(x_i\cdot x_j)-\sum\limits_{i=1}^N\alpha_{i}$ 

​	$s.t.$   $\sum\limits_{i=1}^N\alpha_iy_i=0$ 

​				$\alpha_i\geq 0, i=1,2,\cdots,N$ 