import test
import time
import numpy as np

start_time = time.time()
a = np.random.rand(100, 100) * 2 - 1  # 生成300*300的随即矩阵
b = np.random.rand(100, 100) * 2 - 1
r = np.empty_like(a)  # 创建一个空矩阵，用来存储计算结果
test.main_func(a, b, r, 500000)  # 调用main_func进行测试
end_time = time.time()
print(end_time - start_time)  # 输出时间
print(r)  # 输出运行结果
