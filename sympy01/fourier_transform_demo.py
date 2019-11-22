from tools import *
from sympy import *
from sympy.abc import x, k, f
from sympy.integrals import laplace_transform

# 傅里叶级数
# f = Piecewise((x,x>0),(x,x<pi),(-x,x<0),(-x,x>-pi))
# f = Piecewise((x,(x>0) & (x<pi)),(-x,(x<0) & (x>-pi))) #判断的括号要加
# print(f)
# print(f.subs({x:-5}))
# # f1 = fourier_series(f, (x, -pi, pi))
# # print(f1)
# f2 = fourier_series(f, (x, -pi, pi)).truncate(8)#截断
# print(f2)

# f2 = fourier_transform(x)
# print(f2)
f1 = fourier_transform(exp(-x**2), x, k)
print(f1)
f1 = laplace_transform(sin(x),x,f)
print(f1)