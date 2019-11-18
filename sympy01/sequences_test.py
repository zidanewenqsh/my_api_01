# from tools import *
import sympy
from sympy import *
# from sympy import sequence,SeqFormula,SeqPer


from sympy import sequence, SeqPer, SeqFormula
from sympy.abc import n
a = sequence(n**2, (n, 0, 5))
print(a)
# SeqFormula(n**2, (n, 0, 5))
b = sequence((1, 2, 3, 4), (n, 0, 4))
# SeqPer((1, 2, 3), (n, 0, 5))
print(b)

print(a.coeff(3))#在自变量取特定值时的值
print(a[:])
print(b[:])
print(b.periodical)#周期序列
print(b.period)#周期序列长度

k = sympy.symbols('k')
c = SeqPer((k,k**2,k**3),(k,0,oo))
print(c.periodical)
print(c[0:10])
print(c.coeff(4))

d = SeqFormula(n**3,(n,-oo,0))#不能写0，-oo
print(d[0:6])



print(SeqAdd(SeqPer((1, 2), (n, 0, oo)), S.EmptySequence))
# SeqPer((1, 2), (n, 0, oo))
print(SeqAdd(SeqPer((1, 2), (n, 0, 5)), SeqPer((1, 2), (n, 6, 10))))
# EmptySequence()
print(SeqAdd(SeqPer((1, 2), (n, 0, oo)), SeqFormula(n**2, (n, 0, oo))))
# SeqAdd(SeqFormula(n**2, (n, 0, oo)), SeqPer((1, 2), (n, 0, oo)))
print(SeqAdd(SeqFormula(n**3), SeqFormula(n**2)))
# SeqFormula(n**3 + n**2, (n, 0, oo))

e = SeqAdd(SeqPer((1, 2), (n, 0, oo)), SeqFormula(n**2, (n, 0, oo)))
print(e[0:6])

print(SeqMul(SeqPer((1, 2), (n, 0, oo)), S.EmptySequence))
# EmptySequence()
print(SeqMul(SeqPer((1, 2), (n, 0, 5)), SeqPer((1, 2), (n, 5, 10))))
# EmptySequence()
print(SeqMul(SeqPer((1, 2), (n, 0, oo)), SeqFormula(n**2)))
# SeqMul(SeqFormula(n**2, (n, 0, oo)), SeqPer((1, 2), (n, 0, oo)))
print(SeqMul(SeqFormula(n**3), SeqFormula(n**2)))
# SeqFormula(n**5, (n, 0, oo))

f = SeqMul(SeqPer((1, 2), (n, 0, oo)), SeqFormula(n**2))
print(f[0:6])


