from tool import *
from sympy import *
from sympy.abc import x, k, f
from sympy.integrals import laplace_transform, fourier_transform

f1 = fourier_transform(exp(-x**2), x, k)
print(f1)
f1 = laplace_transform(sin(x),x,f)
print(f1)
# help(laplace_transform)
help(fourier_series)