from tool import *
from sympy import *

# f = Piecewise((x,x>0),(x,x<pi),(-x,x<0),(-x,x>-pi))
f = Piecewise((x,(x>0) & (x<pi)),(-x,(x<0) & (x>-pi))) #判断的括号要加
print(f)
print(f.subs({x:-5}))
f = Piecewise((x,(x>0) & (x<pi)),(-x,(x<0) & (x>-pi)),(0,True)) #范围外为0
print(f)
print(f.subs({x:-5}))
# f = Piecewise((x,(x>0) & (x<pi)),(-x,(x<0) & (x>-pi)),True)
# print(f)
# print(f.subs({x:-5}))