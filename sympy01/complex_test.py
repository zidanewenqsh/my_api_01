from tools import *
from sympy import *
a = cos(x)+I*sin(x)
print(a)
a1=a.subs({x:pi/6})
a2=a.subs({x:pi/3})
print(a1)
print(a2)
b1 = a1*a2
print(b1)
# print(pretty(b1))
print(b1.evalf())
print(exp(I*pi/6).evalf())
print(a1.evalf())