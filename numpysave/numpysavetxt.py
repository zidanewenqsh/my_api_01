from tool import *

a = np.arange(8).reshape(2,4)
b = np.add.accumulate(a)
c = a + b
f = "filename.txt"
np.savetxt(f, a)
np.savetxt(f, b)#没用
d = np.loadtxt(f)
print(d)