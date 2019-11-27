import numpy as np
# from sympy import *
from numpy import cos, sin, pi, sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def get_norm_2(a: np.ndarray, b: np.ndarray):
    if a.shape == b.shape:
        return (a ** 2 + b ** 2) ** (0.5) + 1e-12
    else:
        raise ValueError

# def get_norm_0(a: np.ndarray):
#     return np.sum(a ** 2, axis=-1, keepdims=True) ** (0.5) + 1e-12
def normalize_vector(a: np.ndarray):
    return a / (np.sum(a ** 2, axis=-1, keepdims=True) ** (0.5) + 1e-12)


def rotate_3d(x: np.ndarray, tx=0, ty=0, tz=0, n=1):
    rx = np.array([1, 0, 0, 0, cos(tx), sin(tx), 0, -sin(tx), cos(tx)]).reshape(3, 3)
    ry = np.array([cos(ty), 0, -sin(ty), 0, 1, 0, sin(ty), 0, cos(ty)]).reshape(3, 3)
    rz = np.array([cos(tz), sin(tz), 0, -sin(tz), cos(tz), 0, 0, 0, 1]).reshape(3, 3)
    # print(m)
    # x = np.matmul(x, rx)
    try:
        x = x.reshape(-1, 3)
        if n > 0:
            for _ in range(n):
                # x1 = np.dot(x, rx)
                # x2 = np.dot(x1, ry)
                # x3 = np.dot(x2, rz)
                x = np.matmul(x, rx)  # matmul不支持sympy计算,dot可以
                x = np.matmul(x, ry)
                x = np.matmul(x, rz)
        return x
        # return x.astype('f4')#sympy可以用这个返回
    except:
        raise ValueError


def combined_transform(a: np.ndarray, b: np.ndarray):
    pass


def get_angle(x: np.ndarray, y: np.ndarray):
    '''
    两个向量之间的夹角
    :param x:
    :param y:
    :return:
    '''
    if x.shape[-1] == y.shape[-1]:
        # x = x / np.linalg.norm(x, 2, -1, True)
        # y = y / np.linalg.norm(y, 2, -1, True)
        x = np.expand_dims(x, axis=-2)
        y = np.expand_dims(y, axis=-2)
        # norm_x = np.sum(x ** 2, axis=-1, keepdims=True) ** (0.5) + 1e-12
        # x = x / norm_x
        # norm_y = np.sum(y ** 2, axis=-1, keepdims=True) ** (0.5) + 1e-12
        # y = y / norm_y
        x = normalize_vector(x)
        y = normalize_vector(y)
        y = y.swapaxes(-1, -2)
        # z = np.matmul(x, y)

        return np.squeeze(np.matmul(x, y), axis=-2)
        # return np.matmul(x, y) * np.eye(x.shape[0]) #只看对角线
        # return np.dot(x,y)* np.eye(x.shape[0])
    else:
        raise ValueError


def get_axis_angle(x: np.ndarray, ndim=3):
    '''
    向量与三个坐标轴的夹角
    :param x:
    :param ndim:
    :return:
    '''
    dim = x.shape[-1]

    if dim >= ndim:
        x = x[:, :ndim]
        y = np.eye(ndim).swapaxes(-1, -2)
        # x = x / np.linalg.norm(x, 2, -1, True)
        # norm_x = np.sum(x ** 2, axis=-1, keepdims=True) ** (0.5) + 1e-12
        # x = x / norm_x
        x = normalize_vector(x)

        return np.matmul(x, y)
    else:
        raise ValueError


def get_face_angle(x: np.ndarray):
    '''
    向量与三个坐标平面的夹角
    :param x:
    :return: np.ndarray: yoz, xoz, xoy
    '''
    dim = x.shape[-1]
    if dim >= 3:
        x = x[:, :3]
        y = np.array([[0, 1, 1, 1, 0, 1, 1, 1, 0]]).reshape(3, 3)
        x = x.reshape(-1, 1, 3)
        x = np.expand_dims(x, axis=-2)
        y = x * y
        # 不用np.linalg.norm是为了防止三个都是0的情况
        # norm_y = np.sum(y ** 2, axis=-1, keepdims=True) ** (0.5) + 1e-12
        # y = y / norm_y
        # norm_x = np.sum(x ** 2, axis=-1, keepdims=True) ** (0.5) + 1e-12
        # x = x / norm_x
        x = normalize_vector(x)
        y = normalize_vector(y)
        y = y.swapaxes(-1, -2)

        return np.matmul(x, y).reshape(-1, 3)  # 高维的不能用dot,dot只处理二维. .T会将所有维度转换,
    else:
        raise ValueError


def translation_3d(a, tx=0, ty=0, tz=0):
    '''
    向量平移
    :param a:
    :param tx:
    :param ty:
    :param tz:
    :return:
    '''
    m = np.eye(4)
    m[-1, 0] = tx
    m[-1, 1] = ty
    m[-1, 2] = tz
    a = np.concatenate((a, np.ones((a.shape[0], 1))), axis=1)
    result = np.matmul(a, m)
    return result[:, :-1]


def scalling_3d(a, sx=1, sy=1, sz=1):
    '''
    向量缩放
    :param a:
    :param sx:
    :param sy:
    :param sz:
    :return:
    '''
    m = np.eye(4)
    m[0, 0] = sx
    m[1, 1] = sy
    m[2, 2] = sz
    a = np.concatenate((a, np.ones((a.shape[0], 1))), axis=1)
    result = np.matmul(a, m)
    return result[:, :-1]


def rotate_x_3d(a, t):
    '''
    向量绕x坐标轴旋转
    :param a:
    :param t:角度
    :return:
    '''
    m = np.eye(4)
    m = np.expand_dims(m, axis=0)
    m = m.repeat(a.shape[0], axis=0)
    m[:, 1, 1] = cos(t)
    m[:, 1, 2] = sin(t)
    m[:, 2, 1] = -sin(t)
    m[:, 2, 2] = cos(t)

    a = np.concatenate((a, np.ones((a.shape[0], 1))), axis=1)
    a = np.expand_dims(a, axis=-2)
    result = np.matmul(a, m)
    return np.squeeze(result, axis=-2)[..., :-1]


def rotate_y_3d(a, t):
    '''
    向量绕y坐标轴旋转
    :param a:
    :param t:角度
    :return:
    '''
    m = np.eye(4)
    m = np.expand_dims(m, axis=0)
    m = m.repeat(a.shape[0], axis=0)
    m[:, 0, 0] = cos(t)
    m[:, 0, 2] = -sin(t)
    m[:, 2, 0] = sin(t)
    m[:, 2, 2] = cos(t)

    a = np.concatenate((a, np.ones((a.shape[0], 1))), axis=1)
    a = np.expand_dims(a, axis=-2)
    result = np.matmul(a, m)
    return np.squeeze(result, axis=-2)[..., :-1]


def rotate_z_3d(a, t):
    '''
    向量绕z坐标轴旋转
    :param a:
    :param t:角度
    :return:
    '''
    m = np.eye(4)
    m = np.expand_dims(m, axis=0)
    m = m.repeat(a.shape[0], axis=0)

    m[:, 0, 0] = cos(t)
    m[:, 0, 1] = sin(t)
    m[:, 1, 0] = -sin(t)
    m[:, 1, 1] = cos(t)

    a = np.concatenate((a, np.ones((a.shape[0], 1))), axis=1)
    a = np.expand_dims(a, axis=-2)
    result = np.matmul(a, m)
    return np.squeeze(result, axis=-2)[..., :-1]


def rotate_to_x(a):
    '''
    将向量旋转到x坐标轴
    先沿x轴转到xoz平面，再沿y轴转到x轴
    :param a:
    :return:
    '''
    # x = a[...,0]
    y = a[..., 1]
    z = a[..., 2]
    t = z / get_norm_2(y, z)
    t1 = np.arccos(t)
    a = rotate_x_3d(a, t1)
    x = a[..., 0]
    # y = a[..., 1]
    z = a[..., 2]
    t = x / get_norm_2(x, z)
    t2 = np.arccos(t)
    a = rotate_y_3d(a, t2)
    return a, t1, t2


def rotate_to_y(a):
    '''
    将向量旋转到y坐标轴
    先沿y轴转到xoy平面，再沿z轴转到y轴
    :param a:
    :return:
    '''
    x = a[..., 0]
    # y = a[..., 1]
    z = a[..., 2]
    t = x / get_norm_2(x, z)
    t1 = np.arccos(t)
    a = rotate_y_3d(a, t1)
    x = a[..., 0]
    y = a[..., 1]
    # z = a[..., 2]
    t = y / get_norm_2(x, y)
    t2 = np.arccos(t)
    a = rotate_z_3d(a, t2)
    return a, t1, t2


def rotate_to_z(a):
    '''
    将向量旋转到z坐标轴
    先沿z轴转到yoz平面，再沿x轴转到z轴
    :param a:
    :return:
    '''
    x = a[..., 0]
    y = a[..., 1]
    # z = a[..., 2]
    t = y / get_norm_2(x, y)
    t1 = np.arccos(t)
    a = rotate_z_3d(a, t1)
    # x = a[..., 0]
    y = a[..., 1]
    z = a[..., 2]
    t = z / get_norm_2(y, z)
    t2 = np.arccos(t)
    a = rotate_x_3d(a, t2)
    return a, t1, t2


def rotate_from_x(a, t1, t2):
    '''
    从x坐标轴回到原来位置
    先沿y轴转-t2,再沿x轴转-t1
    :param a:
    :param t1:
    :param t2:
    :return:
    '''
    a = rotate_y_3d(a, -t2)
    a = rotate_x_3d(a, -t1)

    return a


def rotate_from_y(a, t1, t2):
    '''
    从y坐标轴回到原来位置
    先沿z轴转-t2,再沿y轴转-t1
    :param a:
    :param t1:
    :param t2:
    :return:
    '''
    a = rotate_z_3d(a, -t2)
    a = rotate_y_3d(a, -t1)

    return a


def rotate_from_z(a, t1, t2):
    '''
    从z坐标轴回到原来位置
    先沿x轴转-t2,再沿z轴转-t1
    :param a:
    :param t1:
    :param t2:
    :return:
    '''
    a = rotate_x_3d(a, -t2)
    a = rotate_z_3d(a, -t1)

    return a


def rotate_around(a, p, t):
    '''
    绕某一特定的轴旋转
    :param a:(0,a)为转动向量
    :param p:(0,p)为转动轴
    :param t:转动角度
    :return:
    '''

    _, t1, t2 = rotate_to_x(p)
    a1 = rotate_x_3d(a, t1)
    a1 = rotate_y_3d(a1, t2)
    print("a1", a1)
    a1 = rotate_x_3d(a1, t)
    result = rotate_from_x(a1, t1, t2)
    return result


def plot_3d(a):
    x = a[:, 0]
    y = a[:, 1]
    z = a[:, 2]
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
    ax.set_xlim3d(-1, 5)
    ax.set_ylim3d(-1, 5)
    ax.set_zlim3d(-1, 5)
    plt.show()


def plotvecter_3d(a: np.ndarray):
    if a.ndim == 2 and a.shape[-1] >= 3:
        a = np.expand_dims(a, axis=1)
        a = np.concatenate((np.zeros_like(a), a), axis=1)

        # 绘制向量图
        fig = plt.figure()
        ax = Axes3D(fig)
        for i, a_ in enumerate(a):
            x = a_[..., 0]
            y = a_[..., 1]
            z = a_[..., 2]
            ax.plot(x, y, z, label='{0}'.format(i))

        # 添加坐标轴(顺序是Z, Y, X)
        ax.legend()
        ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
        ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
        ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})
        ax.set_xlim3d(0, 5)
        ax.set_ylim3d(0, 5)
        ax.set_zlim3d(0, 5)
        plt.show()
    else:
        raise ValueError


if __name__ == '__main__':
    np.set_printoptions(precision=4, threshold=np.inf, suppress=True)
    tx = 1
    ty = 2
    tz = 3
    m = np.eye(4)
    m[-1, 0] = tx
    m[-1, 1] = ty
    m[-1, 2] = tz
    print(m)
    n = np.sqrt(3)
    print(n)
    a = np.array([[4, 3, 1], [n, n, n]], dtype='f4')
    a1 = np.ones((a.shape[0], 1))
    print(a1)
    a2 = np.concatenate((a, np.ones((a.shape[0], 1))), axis=1)
    # print(a)
    print(a2)
    a3 = translation_3d(a, 1, 2, 3)
    print(a3)
    a4 = scalling_3d(a, 2, 3, 4)
    print(a4)
    t = np.array([pi / 2, pi])
    a5 = rotate_z_3d(a, t)
    print(a5)
    # t = pi / 2
    # m = np.eye(4)
    # m[0, 0] = cos(t)
    # m[0, 1] = sin(t)
    # m[1, 0] = -sin(t)
    # m[1, 1] = cos(t)
    # a = np.concatenate((a, np.ones((a.shape[0], 1))), axis=1)
    # b = np.matmul(a, m)
    # print(b)
    # c = np.matmul(b, m.T)
    # print(c)
    # print(m)
    # print(m.T)
    a6, t1, t2 = rotate_to_z(a)
    print(a6)
    print(t1)
    print(t2)
    a7 = rotate_from_z(a6, t1, t2)
    print(a7)
    a = np.array([[1, 2, 3], [3, 3, 1]])
    p = np.array([[1, 1, 1]])
    t = pi / 2
    b = rotate_around(a, p, t)
    print(b)
    d = np.concatenate((a, p, b), axis=0)
    print(d)
    print(get_angle(a, p), get_angle(p, b))
    e = get_angle(a, p)
    print(e.shape)
    print(e)
    print(get_axis_angle(a))
    print(get_face_angle(a))
