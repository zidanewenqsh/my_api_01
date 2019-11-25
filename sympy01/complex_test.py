from tools import *
from sympy import *

a = cos(x) + I * sin(x)
print(a)
a1 = a.subs({x: pi / 6})
a2 = a.subs({x: pi / 3})
print(a1)
print(a2)
b1 = a1 * a2
print(b1)
# print(pretty(b1))
print(b1.evalf())
print(exp(I * pi / 6).evalf())
print(a1.evalf())
print('---------')

a = cos(x)
b = sin(x)
e1 = (exp(I * x) + exp(-I * x)) / 2
e2 = (exp(I * x) - exp(I * (-x))) / (2*I)

print(a.subs({x: pi / 6}).evalf(chop=True))
print(b.subs({x: pi / 6}).evalf(chop=True))
print(e1.subs({x: pi / 6}).evalf(chop=True))
print(e2.subs({x: pi / 6}).evalf(chop=True))
