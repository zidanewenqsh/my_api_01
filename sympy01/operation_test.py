from tools import *
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

# 级数展开
tmp = series(exp(I * x), x, 0, 10)
print(tmp)
tmp1 = series(cos(x), x, 0, 10)
print(tmp1)
# 级数的实部
print(re(tmp))
# 级数的虚部
print(im(tmp))

# 傅里叶级数
# f = Piecewise((x,x>0),(x,x<pi),(-x,x<0),(-x,x>-pi))
f = Piecewise((0,(x>0) & (x<pi)),(x,(x<0) & (x>-pi))) #判断的括号要加
print(f)
print(f.subs({x:-1}))
f1 = fourier_series(f, (x, -pi, pi))
print(f1)
f2 = fourier_series(f, (x, -pi, pi)).truncate(8)#截断
print(f2)

# f2 = fourier_transform(x)
# print(f2)

# SeqFormula

n = Symbol('n')
s = SeqFormula(n**2, (n, 0, 5))
print(s.formula)
