import numpy as np
print(np.add.reduce([1,2,3])) #6
print(np.add.accumulate([1,2,3])) #[1 3 6]
print(np.add.accumulate([[1,2,3],[4,5,6]], axis=0))
print(np.add.accumulate([[1,2,3],[4,5,6]], axis=1))
a = np.array([1,2,3,4])
result = np.add.reduceat(a,indices=[0,1,0,2,0,3,0])
print(result)
# if indices[i] < indices[i+1]:
#     result[i] = np.reduce(a[indices[i]:indices[i+1]])
# else:
#     result[i] = a[indices[i]
a = np.multiply.outer([1,2,3,4,5],[2,3,4])
print(a)
# outer : 只按照一维数组进行计算，如果传入参数是多维数组，则先将此数组展平为一维数组之
# 后再进行运算。outer乘积计算的列向量和行向量的矩阵乘积
# [[ 2  3  4]
#  [ 4  6  8]
#  [ 6  9 12]
#  [ 8 12 16]
#  [10 15 20]]
a = np.arange(12).reshape(2,3,2)
b = np.arange(24).reshape(4,3,2)
c = np.inner(a,b)
print(c.shape)
print(a.shape)
print(b.shape)
# print(c)
# (2, 3, 2, 3)
print(c[0,0,0,0] == np.inner(a[0,0],b[0,0]))
# True
print(c[0,1,1,0] == np.inner(a[0,1],b[1,0]))
# True
print(c[1,2,1,2] == np.inner(a[1,2],b[1,2]))
# True