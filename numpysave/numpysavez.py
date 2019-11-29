from tool import *

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