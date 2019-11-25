import sympy
import numpy as np
from sympy import *
from numpy import linalg
x1,x2,x3,x4=1,2,3,4
a = np.array([[x1,x2,x3,x4]])
b = np.concatenate((a**0,a**1,a**2,a**3),axis=0)
print(b)
c = linalg.det(b)
print(c)
b1 = b.T
print(b1)