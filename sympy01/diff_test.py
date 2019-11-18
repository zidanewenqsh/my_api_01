from tools import *
from sympy import *
# from sympy01.abc import x,y,z
'''
求导'''
z = exp(x)+x**2
d1 = diff(z,x)
d2 = diff(z,x,2)
print(d1)
print(d1.evalf(subs={x:1}))
print(d2)

z = y*exp(x)+y**2
d3 = diff(z,x)
d4 = diff(z,y)
print(d3)
print(d4)
