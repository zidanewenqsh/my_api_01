import test
import numpy as np
import time
import math
import ctypes


def app1(x):
    a = 0
    for i in range(1, x + 1):
        a += np.log(i)
    return a


def app2(x):
    a = 0
    for i in range(1, x + 1):
        # print(i)
        # print("log",i,math.log(i))
        a += math.log(i)
        # print("a",a)
    return a


dll = ctypes.windll.LoadLibrary("app3.dll")
app_3 = dll.app3
app_3.argtypes = [ctypes.c_double, ]
app_3.restype = ctypes.c_double

if __name__ == '__main__':
    a = 10000000
    print(math.log(np.e))
    t1 = time.time()
    b0 = test.app(a)
    print("b0", b0)
    t2 = time.time()
    time0 = t2 - t1
    print("time0", time0)

    t1 = time.time()
    b1 = app1(a)
    print("b1", b1)
    t2 = time.time()
    time1 = t2 - t1
    print("time1", time1)

    t1 = time.time()
    b2 = app2(a)
    print("b2", b2)
    t2 = time.time()
    time2 = t2 - t1
    print("time2", time2)

    t1 = time.time()
    b3 = app_3(a)
    print("b3", b3)
    t3 = time.time()
    time3 = t2 - t1
    print("time3", time3)
