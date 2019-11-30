import numpy as np

# print(np.add.reduce([1,2,3])) #6
# print(np.add.accumulate([1,2,3])) #[1 3 6]
# print(np.add.accumulate([[1,2,3],[4,5,6]], axis=0))
# print(np.add.accumulate([[1,2,3],[4,5,6]], axis=1))
# a = np.array([1,2,3,4])
'''
reduceat方法需要输入一个数组以及一个索引值列表作为参数
B3 = np.add.reduceat(B,[0,5,2,7])
print (B3)
# [10 5 20 15]
# 解析：第一步用到索引值列表中的0和5，实际上就是对数组中索引值在0到5之间的元素进行reduce操作。
print (np.add.reduce(B[0:5]))
# 第二步用到索引值5和2。由于2比5小，所以直接返回索引值为5的元素
print (np.add.reduce(B[5]))
# 第三步用到索引值2和7。这一步是对索引值在2到7之间的数组元素进行reduce操作
print (np.add.reduce(B[2:7]))
# 第四步用到索引值7。这一步是对索引值从7开始直到数组末端的元素进行reduce操作
print (np.add.reduce(B[7:]))
'''


def answer(a):
    result = np.zeros_like(a)
    result.flat = 42
    return result

ufunc = np.frompyfunc(answer, 1, 1)
print(ufunc(np.arange(4))[0])

a = np.arange(10)
result = np.add.reduceat(a,indices=[0,5,2,7])
# print(result)
# if indices[i] < indices[i+1]:
#     result[i] = np.reduce(a[indices[i]:indices[i+1]])
# else:
#     result[i] = a[indices[i]

'''
inner : 和dot乘积一样，对于两个一维数组，计算的是这两个数组对应下标元素的乘积和；
对于多维数组，它计算的结果数组中的每个元素都是：数组a和b的最后一维的内积，
因此数组a和b的最后一维的长度必须相同：
等价于np.matmul(a,b.T)

outer : 只按照一维数组进行计算，如果传入参数是多维数组，则先将此数组展平为一维数组之后再进行运算。
outer乘积计算的列向量和行向量的矩阵乘积
'''
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
b = np.arange(6).reshape(3,2)
c = np.inner(a,b)

print(c.shape)
print(a.shape)
print(b.shape)
print(a)
print(b)
print(c)
print(np.matmul(a,b.T))
# print(np.inner([1,2,3,4],[5,6,7,8]))
# # print(c)
# (2, 3, 2, 3)
# print(c[0,0,0,0] == np.inner(a[0,0],b[0,0]))
# # True
# print(c[0,1,1,0] == np.inner(a[0,1],b[1,0]))
# # True
# print(c[1,2,1,2] == np.inner(a[1,2],b[1,2]))
# # True