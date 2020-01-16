import ctypes

dll = ctypes.cdll.LoadLibrary(r"D:\PycharmProjects\my_api_01\cpython\untitled.dll")
fun = dll.hello
# fun.argtypes = (ctypes.c_long,)
# fun.restype = ctypes.c_longlong
# x = 100
# y = fun(x)
# print(y)
# fun()