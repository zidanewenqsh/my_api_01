from tools import *
from sympy import *

t = Symbol('t')
f = 2 * t
#不定积分
i = integrate(f, t)
i1 = integrate(i,t)
print(i)
print(i1)
#二重定积分
g = integrate(f, (t, 0, x))
print(g)
i2 = integrate(g, (x, 0, 3))
print(i2)
#值代换
f_ = f.evalf(subs={t:2},n=4)
print(f_)