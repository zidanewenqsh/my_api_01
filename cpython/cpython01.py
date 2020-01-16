import ctypes

dll = ctypes.cdll.LoadLibrary(r"test001.dll")
fun = dll.cal_num
fun.argtypes = (ctypes.c_long,)
fun.restype = ctypes.c_longlong
x = 2
y = fun(x)
print(y)
