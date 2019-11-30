import numpy as np
'''
np.save
np.load
变量一个一个的存，一个一个的取
'''
a = np.arange(8)
b = np.add.accumulate(a)
c = a + b
# f = open("result.npy", "wb")
# np.save(f, a) # 顺序将a,b,c保存进文件对对象f
# np.save(f, b)
# np.save(f, c)
# f.close()
f = open("result.npy", "rb")
print(np.load(f)) # 顺序从文件对象f中读取内容
# array([0, 1, 2, 3, 4, 5, 6, 7])
print(np.load(f))
# array([ 0, 1, 3, 6, 10, 15, 21, 28])
print(np.load(f))
# array([ 0, 2, 5, 9, 14, 20, 27, 35])
f.close()