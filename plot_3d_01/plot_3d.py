import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图

datafile = '../datas/data.txt'
x = []
y = []
z = []
with open(datafile) as f1:
    for lines in f1.readlines():
        data_ = lines.strip().split()
        x.append(float(data_[0]))
        y.append(float(data_[1]))
        z.append(float(data_[2]))
print(len(x))
print(len(y))
print(len(z))

# 绘制散点图
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z)
# plt.scatter(x,y,z)#RuntimeWarning: invalid value encountered in sqrt
#   scale = np.sqrt(self._sizes) * dpi / 72.0 * self._factor
# 添加坐标轴(顺序是Z, Y, X)
ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})
ax.set_xlim3d(-5,5)
ax.set_ylim3d(0,15)
ax.set_zlim3d(-3,3)
plt.show()
