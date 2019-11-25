from tools import *
from sympy import *
'''
求极限'''

f1 = sin(x) / x
l1 = limit(f1, x, 0)
f2 = (1 + 1 / x) ** x
l2 = limit(f2, x, oo)

print(l1)
print(l2)
