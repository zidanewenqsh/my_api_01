from tool import *
from sympy import *
#误差函数
a = erf(0.5).evalf(n=10)
print(a)
#正弦积分函数
a = Si(1).evalf(n=10)
print(a)