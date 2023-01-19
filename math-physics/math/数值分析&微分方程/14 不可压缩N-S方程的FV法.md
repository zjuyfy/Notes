> **定义**1（domain）
>
> domain是一个连通且有界的正则开子集 $\Omega\in\mathbb R^D,D=2,3$

> **定义**2（欧拉加速度）
>
> 不可压缩N-S方程(INSE)的欧拉加速度是时间导数的向量：[^$\nabla\vec u$] 
> $$
> \vec a:=\frac{\part\vec u}{\part t},\quad\vec a^*:=-\vec u\cdot\nabla\vec u+\vec g+\nu\Delta \vec u
> $$

> **定义**3（压力泊松方程PPE）
>
> 压力泊松方程(PPE)是一个椭圆方程，描述了INSE中压力与速度之间的关系：
> $$
> \Delta p=\nabla\cdot (\vec g-\vec u\cdot\nabla \vec u)\quad	x\in\Omega\\
> \hat n\cdot \nabla p=\hat n\cdot(\vec a^*-\vec a)\quad x\in\part\Omega
> $$



----

# 勒雷-亥姆霍兹投影

> **定义**4（投影）
>
> 投影 $\bar P$ 是一个从向量空间到自身的线性变换，它满足幂等条件
> $$
> \bar P^2=\bar P
> $$

> **定义**5（勒雷-亥姆霍兹投影）
>
> 见流体力学纳维斯托克斯方程的定义12。

> **定义**5
>
> 在域Ω上向量场v的不可穿透条件为第一类齐次边界条件。

> **定义**5（勒雷投影的四阶近似离散算子）
>
> 与勒雷投影对应的四阶近似投影是离散算子
> $$
> \operatorname P=\operatorname I-\operatorname G\operatorname L^{-1}\operatorname D
> $$

> **定义**6（FV内积）
>
> FV标量内积和在域Ω上的FV向量内积分别为
> $$
> \begin{aligned}
> \langle\phi, \psi\rangle_{S} &=h^{\mathrm{D}} \sum_{\vec{i}}\langle\phi\rangle_{\vec{i}}\langle\psi\rangle_{\vec{i}} \\
> \langle\vec{v}, \vec{w}\rangle_{V} &=h^{\mathrm{D}} \sum_{\vec{i}}\langle\vec{v}\rangle_{\vec{i}} \cdot\langle\vec{w}\rangle_{\vec{i}}
> \end{aligned}
> $$
>
> > **性质**
> >
> > 周期domain上有
> > $$
> > \langle\operatorname D\vec u, \phi\rangle_{S}=\langle\vec{u}, \operatorname G\phi\rangle_{V}
> > $$
> > 因此，对于两个离散算子的矩阵形式有
> > $$
> > \operatorname G=-\operatorname D^T
> > $$
> >
> > > $$
> > > \operatorname G\operatorname L=\operatorname L\operatorname G\\
> > > \operatorname P\operatorname L=\operatorname L\operatorname P
> > > $$
> >
> > > $$
> > > \rho(\operatorname P)=||\operatorname P||_2=1
> > > $$



----

# 周期域上的INSE

> **定理**1
>
> 周期域上的四阶近似INSE为
> $$
> \frac{\mathrm{d}\langle\vec{u}\rangle}{\mathrm{d} t}=\operatorname{P}(-\operatorname{D}\langle\vec{u} \vec{u}\rangle+\langle\vec{g}\rangle+\nu \operatorname{L}\langle\vec{u}\rangle)
> $$

> **算法**1
>
> 将ERK-ESDIRK IMEX RK算法直接应用于ODE系统定理1，得到了一种在周期域上求解INSE的四阶FV方法









-----



[^$∇u→\nabla\vec u$]: 我们用 $\nabla \vec u$ 代表张量 $\part_iu_j$. 