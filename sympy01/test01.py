from tools import *
from sympy import *

n = Symbol('n')
s = SeqFormula(n**2, (n, 0, 5))
print(s.formula)
print(s)