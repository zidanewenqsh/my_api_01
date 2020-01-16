import ctypes

dll = ctypes.cdll.LoadLibrary(r"D:\PycharmProjects\my_api_01\cpython\Dll3.dll")
# print(dll.__class__)
fun = dll.ap
fun.argtypes = (ctypes.c_float,)
fun.restype = ctypes.c_float
x = 2
y = fun(x)
print(y)
