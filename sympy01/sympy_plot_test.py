from sympy import *
from sympy.plotting import plot,plot_parametric
x = symbols('x')
expr = sin(2*sin(x**3))
plot(expr,(x,-5,5))
init_printing()
a = Integral(sqrt(1/x),x)
print(a)
b = pretty(expr)
print(b)
pprint(b)#效果等同于pretty