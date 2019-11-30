import numpy as np

'''
如果你想将多个数组保存到一个文件中的话，可以使用numpy.savez函数。
savez函数的第一个参数是文件名，其后的参数都是需要保存的数组，也可以使用关键字参数为数组起一个名字，
非关键字参数传递的数组会自动起名为arr_0, arr_1, …。savez函数输出的是一个压缩文件(扩展名为npz)，
其中每个文件都是一个save函数保存的npy文件，文件名对应于数组名。load函数自动识别npz文件，
并且返回一个类似于字典的对象，可以通过数组名作为关键字获取数组的内容：
'''
a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)

np.savez("result.npz", a, b, sin_array = c, abc=c)
r = np.load("result.npz")
print(r["arr_0"] )# 数组a
# array([[1, 2, 3],
# [4, 5, 6]])
print(r["arr_1"]) # 数组b
# array([ 0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
print(r["sin_array"]) # 数组c
# array([ 0. , 0.09983342, 0.19866933, 0.29552021, 0.38941834,
# 0.47942554, 0.56464247, 0.64421769, 0.71735609, 0.78332691])
print(r['abc'])
print(type(r))
print(r)
print(len(r))