import ctypes

dll = ctypes.windll.LoadLibrary("app3.dll")
app_3 = dll.app3
app_3.argtypes = [ctypes.c_double,]
app_3.restype = ctypes.c_double
print(app_3(10))