from tool import *
a = np.arange(0,12)
a.shape = 3,4
print(a)
# array([[ 0, 1, 2, 3],
# [ 4, 5, 6, 7],
# [ 8, 9, 10, 11]])

a.tofile("a.bin")
b = np.fromfile("a.bin", dtype=np.float) # 按照float类型读入数据
print(b) # 读入的数据是错误的
# array([ 2.12199579e-314, 6.36598737e-314, 1.06099790e-313,
# 1.48539705e-313, 1.90979621e-313, 2.33419537e-313])
print(a.dtype) # 查看a的dtype
# dtype('int32')
b = np.fromfile("a.bin", dtype=np.int32) # 按照int32类型读入数据
print("b",b) # 数据是一维的
# array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
b.shape = 3, 4 # 按照a的shape修改b的shape
print(b) # 这次终于正确了
# array([[ 0, 1, 2, 3],
# [ 4, 5, 6, 7],
# [ 8, 9, 10, 11]])
np.save("a.npy", a)
c = np.load( "a.npy" )
print(c)
print(type(c),c.dtype)