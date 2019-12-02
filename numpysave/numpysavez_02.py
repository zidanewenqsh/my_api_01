import numpy as np
import time
import pickle
import torch

'''
如果你想将多个数组保存到一个文件中的话，可以使用numpy.savez函数。
savez函数的第一个参数是文件名，其后的参数都是需要保存的数组，也可以使用关键字参数为数组起一个名字，
非关键字参数传递的数组会自动起名为arr_0, arr_1, …。savez函数输出的是一个压缩文件(扩展名为npz)，
其中每个文件都是一个save函数保存的npy文件，文件名对应于数组名。load函数自动识别npz文件，
并且返回一个类似于字典的对象，可以通过数组名作为关键字获取数组的内容：
'''
'''
np.savez
pickle 在数据比较规则时感觉速度较快(比如形状为100)，
torch用numpy.savez文件存比存numpy数据的文件小不少,读写时间也短
'''
np.set_printoptions(precision=2, threshold=1000, suppress=True)
datalist = []
datalist_t = []
# for i in range(10):
#     datalist.append()
a = np.array([1, 2, 3])
b = np.array([2, 2, 3])
c = np.array([3, 2, 3])

num = 500
for i in range(1*num):
    datalist.append(np.random.randn(num, num))

for i in range(1*num):
    datalist_t.append(torch.randn(num, num))

data_arr = np.stack(datalist, axis=0)
data_torch = torch.stack(datalist_t, dim=0)
print(data_arr.shape)
print(type(data_arr), type(data_torch))

t1 = time.time()
np.savez("numpy.npz", data_arr)
# np.savez("result2.npz", [x for x in datalist])#这种写法与上面差不多

t2 = time.time()
t = t2 - t1
print("numpysavetime", t)

t1 = time.time()
np.savez("torch.npz", data_torch)
# np.savez("result2.npz", [x for x in datalist])#这种写法与上面差不多

t2 = time.time()
t = t2 - t1
print("torchsavetime", t)

t1 = time.time()
with open("data.pickle", 'wb') as f1:  # 'w' TypeError: write() argument must be str, not bytes
    pickle.dump(data_arr, file=f1)
    # pickle.dump([x for x in datalist],file=f1)#在pickle.dump中用列表推导式与先遍历再dump不同，会增加一个列表
    # for x in datalist:
    # print(x)
    # pickle.dump(x,file=f1)
t2 = time.time()
t = t2 - t1
print("picklesavetime", t)

t1 = time.time()
# for x in r.values():
#     print(x)
# print([x for x in datalist])
r = np.load("numpy.npz")
for k, v in r.items():
    print(k)
    # print(v)
    print(v.shape)
t2 = time.time()
t = t2 - t1
print("numpyloadtime", t)

t1 = time.time()
# for x in r.values():
#     print(x)
# print([x for x in datalist])
r = np.load("torch.npz")
dataset = []
for k, v in r.items():
    print(k)
    print(v.shape)
    v = torch.from_numpy(v).cuda()
    print(v[0, 0, 0:10])
#     dataset.append(torch.from_numpy(v))
# dataset = torch.stack(dataset,dim=0)
# print(dataset.size())

# print(v)#savez保存的都是Numpy数据

t2 = time.time()
t = t2 - t1
print("torchloadtime", t)

t1 = time.time()
datalist1 = []
with open("data.pickle", 'rb') as f2:
    a = pickle.load(f2)
    # while True:
    #     try:
    #         datalist1.append(pickle.load(f2))
    #     except:
    #         break
print(type(a))
# for x in datalist1:
#     print(x)
t2 = time.time()
t = t2 - t1
print("pickleloadtime", t)
