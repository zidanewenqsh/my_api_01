import numpy as np
import matplotlib.pyplot as plt
# def func(i):
#     return i%4+1
# print(np.fromfunction(func, (10,)))
'''
 frompyfunc和vectorize之间的差异:暂不明
 '''
#这里的参数func指的是你要使用的函数，第二个参数为func中的参数个数，第三个参数为func中的返回值的个数
def triangle_func(c, c0, hc):
    def trifunc(x):
        x = x - int(x) # 三角波的周期为1，因此只取x坐标的小数部分进行计算
        if x >= c: r = 0.0
        elif x < c0: r = x / c0 * hc
        else: r = (c-x) / (c-c0) * hc
        return r
    # 用trifunc函数创建一个ufunc函数，可以直接对数组进行计算, 不过通过此函数
    # 计算得到的是一个Object数组，需要进行类型转换
    return np.frompyfunc(trifunc, 1, 1)
x = np.linspace(0, 2, 1000)
y2 = triangle_func(0.6, 0.4, 1.0)(x)
# print(y2)
plt.plot(x,y2)
plt.show()
plt.pause(0.1)
