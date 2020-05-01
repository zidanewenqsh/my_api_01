'''
@Descripttion: 
@version: 
@Author: QsWen
@Date: 2020-02-13 00:24:48
@LastEditors: QsWen
@LastEditTime: 2020-04-20 17:38:07
'''
import numpy as np
import matplotlib.pyplot as plt


def plotvecter_2d(a: np.ndarray, xlim=(-10,10), ylim=(-10,10), needshow=False):
    if a.ndim == 2 and a.shape[-1] >= 2:
        a = np.expand_dims(a, axis=1)
        print(a.shape)
        a = np.concatenate((np.zeros_like(a), a), axis=1)
        for i, a_ in enumerate(a):
            x = a_[..., 0]
            y = a_[..., 1]
            plt.plot(x, y, label='{0}'.format(i))

        # 添加坐标轴(顺序是Z, Y, X)
        plt.legend()
        plt.ylabel('Y', fontdict={'size': 15, 'color': 'red'})
        plt.xlabel('X', fontdict={'size': 15, 'color': 'red'})
        plt.xlim(*xlim)
        plt.ylim(*ylim)
        if needshow:
            plt.show()
    else:
        raise ValueError

def get_distance(a,b):
    '''
    计算距离
    :param a:
    :param b:
    :return:
    '''
    return np.sum((b-a)**2,axis=-1)**(0.5)

def get_angle(x: np.ndarray, y: np.ndarray):
    '''
    两个向量之间的夹角
    :param x:
    :param y:
    :return:
    '''

    def normalize_vector(a: np.ndarray):
        return a / (np.sum(a ** 2, axis=-1, keepdims=True) ** (0.5) + 1e-12)

    if x.shape[-1] == y.shape[-1]:
        x = np.expand_dims(x, axis=-2)
        y = np.expand_dims(y, axis=-2)

        x = normalize_vector(x)
        y = normalize_vector(y)
        y = y.swapaxes(-1, -2)

        return np.squeeze(np.matmul(x, y), axis=-2)
    else:
        raise ValueError

# def get_length(a):
#     '''
#     计算距离
#     :param a:
#     :param b:
#     :return:
#     '''
#     return np.sum((b-a)**2,axis=-1)**(0.5)

# a = np.array([3,4,2,3]).reshape(2,2)
a = np.array([2.,3]).reshape(-1,2)
v = np.array([1, 1,-1, 1]).reshape(2,2)
v = v/np.sqrt(2)
# v = np.array([1,0,0,1]).reshape(2,2)
print("a",a)
# print(v)

b = np.dot(a,v.T)
print("b",b)

c = np.dot(b,v)
print("c", c)
xlim=(-2,10)
ylim=(-1,5)
needshow=False
plotvecter_2d(a,xlim,ylim,needshow)
plotvecter_2d(v,xlim,ylim,needshow)
plotvecter_2d(b,xlim,ylim,needshow)
l1 = get_distance(np.zeros_like(a),a)
print(l1)
l2 = get_distance(np.zeros_like(b),b)
print(l2)
# print(get_distance(np.zeros_like(v),v))
# plt.show()
# plt.pause(0.1)
a = np.random.randn(4,2)*3
print(a)
# plotvecter_2d(a,needshow=True)
plt.clf()
plt.plot(a[:,0],a[:,1])
plt.show()