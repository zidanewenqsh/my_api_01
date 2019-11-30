import numpy as np

'''
np.add.accumulate
np.add.reduce

[[ 0  1  3  6]
 [ 4  9 15 22]]
[ 6 22]
'''
a = np.arange(8).reshape(2,4)
b = np.add.accumulate(a, axis=1)
c = np.add.reduce(a,axis=1)
print(b)
print(c)

