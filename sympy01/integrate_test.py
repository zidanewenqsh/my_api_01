from tools import *
from sympy import *

t = Symbol('t')
f = 2 * t
#不定积分
i = integrate(f, t)
i1 = integrate(i, t)
i2 = integrate(f,t,t)#二重不定积分
print(i)
print(i1)
print("i2",i2)

#多重积分
i = integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))
print(i)

#二重定积分
g = integrate(f, (t, 0, x))
print(g)
i2 = integrate(g, (x, 0, 3))
print(i2)
i3 = integrate(f,(t, 0, x),(x, 0, 3))
print("i3",i3)
#值代换
f_ = f.evalf(subs={t:2},n=4)
print(f_)

f1 = integrate(x**y*exp(-x), (x, 0, oo))
print(f1)
print(gamma(y+1))
print(re(y))