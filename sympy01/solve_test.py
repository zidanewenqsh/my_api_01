from tools import *
from sympy import *

y = x**2+1

a = solve(y,x)
print(a)
'''
符号表达式会向下传递'''
z = y+3
b = solve(z,y)
print(b)

x,y,z = symbols('x y z')
z = [x+y-3,y-x-1]
c = solve(z,[x,y])
print(c)

#解微分方程
f = Function('f')
a = dsolve(diff(f(x), x) - 2 * x)
print(a)

