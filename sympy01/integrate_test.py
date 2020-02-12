from tool import *
from sympy import *
x,y,z = symbols('x y z')
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

print("------------------------")
u,a = symbols('u a')
expr = 1/(u**2+a**2)**2
expr = 1/sec(u)**2
f1 = integrate(expr,u)
print(f1)
expr1 = 1/(u**2+a**2)
expr2 = ((u*a)/(a**2+u**2))/(2*a**3)
f2 = diff(expr1,u)
f3 = diff(expr2,u)
print(f2)
print(f3)
print("------------------------")
x = symbols('x')
expr = pi*(E-exp(x))**2
# expr = pi*((E*x-E)**2-(exp(x)-E)**2)
f1 = integrate(expr,(x,0,1))
print(f1)
