from tool import *
from sympy import *
x = symbols("x")
# 级数展开
tmp = series(exp(I * x), x, 0, 10)
print(tmp)
tmp1 = series(cos(x), x, 0, 10)
print(tmp1)
# 级数的实部
print(re(tmp))
print("-------")
# 级数的虚部
print(im(tmp))
print("*******")
a = series(sin(x)) # 默认余项次数为6，在 x=0 处展开
print(a)
# x - x**3/6 + x**5/120 + O(x**6)
a = series(exp(x), x, 1, n= 3)#在 x=1 处展开，余项次数为3
print(a)
# E + E*(x - 1) + E*(x - 1)**2/2 + O((x - 1)**3, (x, 1))
a = sin(x).series(x,0,n=4)
print(a)
# sin(1) + (x - 1)*cos(1) - (x - 1)**2*sin(1)/2 + O((x - 1)**3, (x, 1))
'''极限的方向也是用dir参数表示，"+"表示右极限，"-"表示左极限，
series(expr, x=None, x0=0, n=6, dir='+')'''

# 级数求和
i, n = var("i n")
a = summation(i, (i, 1, n)) #summation函数用于级数求和
print(a)
# n**2/2 + n/2
a = summation(1/n, (n, 1, +oo)) # 调和级数，发散
print(a)
# oo
r = symbols('r')
a = summation(1/n**r, (n, 1, +oo)) # 仅当r>1时 收敛
print(a)
# Piecewise((zeta(r), r > 1), (Sum(n**(-r), (n, 1, oo)), True))
