import numpy as np
'''
np.savetxt
np.loadtxt
一个txt只能存一次，下一次会覆盖
'''
a = np.arange(8).reshape(2,4)
b = np.add.accumulate(a, axis=1)
c = a + b
f = "result.txt"
# np.savetxt(f, a)
np.savetxt(f, b, fmt="%.2f")
d = np.loadtxt(f)
print(d)
print(a)
print(b)

a = np.arange(0,12,0.5).reshape(4,-1)
np.savetxt("a.txt", a) # 缺省按照'%.18e'格式保存数据，以空格分隔
b = np.loadtxt("a.txt")
print(b)
# array([[ 0. , 0.5, 1. , 1.5, 2. , 2.5],
# [ 3. , 3.5, 4. , 4.5, 5. , 5.5],
# [ 6. , 6.5, 7. , 7.5, 8. , 8.5],
# [ 9. , 9.5, 10. , 10.5, 11. , 11.5]])
np.savetxt("b.txt", a, fmt="%d", delimiter=",") #改为保存为整数，以逗号分隔
c = np.loadtxt("b.txt",delimiter=",") # 读入的时候也需要指定逗号分隔
print(c)
# array([[ 0., 0., 1., 1., 2., 2.],
# [ 3., 3., 4., 4., 5., 5.],
# [ 6., 6., 7., 7., 8., 8.],
# [ 9., 9., 10., 10., 11., 11.]])