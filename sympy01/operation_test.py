from tool import *
from sympy import *

n = symbols('n')
# 求和
s = summation(1 / factorial(n), (n, 1, 100))
print(s.evalf())
# 阶乘
a = factorial(5)
print(a)
'''
evalf'''
a = sympy.Symbol('a')
print((1 / a).evalf(subs={a: 3}, n=10))  # 值代换，保留小数位数

# 欧拉公式和复数
# E**(I*pi) + 1
x = symbols("x", real=True)
y = expand(E ** (I * x), complex=True)
print(x)
print(y)
print(y.evalf(subs={x: pi}, n=3, chop=False))  # -1.0 + 0.e-16*I
print(y.evalf(subs={x: pi}, n=3, chop=True))  # -1.00




