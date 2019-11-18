from tools import *
from sympy import *
from sympy.abc import x, k

# 傅里叶级数
# f = Piecewise((x,x>0),(x,x<pi),(-x,x<0),(-x,x>-pi))
f = Piecewise((x,(x>0) & (x<pi)),(-x,(x<0) & (x>-pi))) #判断的括号要加
print(f)
print(f.subs({x:-5}))
# f1 = fourier_series(f, (x, -pi, pi))
# print(f1)
f2 = fourier_series(f, (x, -pi, pi)).truncate(8)#截断
print(f2)

# f2 = fourier_transform(x)
# print(f2)
print("---------")
s = fourier_series(x**2, (x, -pi, pi))
s1 = s.scale(2).truncate()
print(s1)
# -8*cos(x) + 2*cos(2*x) + 2*pi**2/3

s = fourier_series(x**2, (x, -pi, pi))
s1 = s.scalex(2).truncate()
print(s1)
# -4*cos(2*x) + cos(4*x) + pi**2/3

s = fourier_series(x**2, (x, -pi, pi))
s1 = s.shift(1).truncate()
print(s1)
# -4*cos(x) + cos(2*x) + 1 + pi**2/3

s = fourier_series(x**2, (x, -pi, pi))
s1 = s.shiftx(1).truncate()
print(s1)
# -4*cos(x + 1) + cos(2*x + 2) + pi**2/3