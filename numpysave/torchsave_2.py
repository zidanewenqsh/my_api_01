# import numpy as np
import time
import pickle
import torch
import torch.nn as nn
from torch.utils import data

'''
Result
D:\MySoft\Anaconda3\python.exe D:/PycharmProjects/my_api_01/numpysave/torchsave_2.py
torchsavetime 158.62256288528442
data_torchdeletetime 1.431159257888794
datasettime 195.4024841785431
datasetdeletetime 1.3989815711975098
dataloadertime 98.83431911468506
'''

class Dataset(data.Dataset):
    def __init__(self, path):
        super(Dataset, self).__init__()
        # self.path = path
        # self.dataset = []
        self.dataset = torch.load(path)

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        return self.dataset[index]


# np.set_printoptions(precision=2, threshold=1000, suppress=True)

N, C, H, W = 4000, 3, 416, 416
data_torch = torch.randn(N, C, H, W)

t1 = time.time()
torch.save(data_torch,"datas3.torch")

t2 = time.time()
t = t2 - t1
print("torchsavetime", t)

t1 = time.time()
del data_torch #清内存
t2 = time.time()
t = t2 - t1
print("data_torchdeletetime", t)
# t1 = time.time()
# ds = torch.load(r"D:\PycharmProjects\my_api_01\numpysave\datas2.torch")
# print(ds.size())
# t2 = time.time()
# t = t2 - t1
# print("torchloadtime", t)

#
# print(r.values()[0])#TypeError: 'ValuesView' object is not subscriptable
# dataset = []
# for k, v in r.items():
#     print(k)
#     print(v.shape)
#     v = torch.from_numpy(v).cuda()
#     print(v[0, 0, 0, 0:10])
# t2 = time.time()
# t = t2 - t1
# print("torchloadtime", t)

t1 = time.time()
dataset = Dataset(r"D:\PycharmProjects\my_api_01\numpysave\datas3.torch")
print(type(dataset))
print(len(dataset))
torch.save(dataset, "dataset3.torch")
t2 = time.time()
t = t2 - t1
print("datasettime", t)
t1 = time.time()
del dataset #清内存
t2 = time.time()
t = t2 - t1
print("datasetdeletetime", t)

# t1 = time.time()
# dataset_ = torch.load("dataset.torch")
# print(type(dataset))
# t = t2 - t1
# print("datasetloadtime", t)

t1 = time.time()
dataloader = data.DataLoader(torch.load("dataset3.torch"), 100, True, drop_last=True)
print(len(dataloader))
for i, v in enumerate(dataloader):
    print(v.size(), type(v))
    break
t2 = time.time()
t = t2 - t1
print("dataloadertime", t)

# t1 = time.time()
#
# t2 = time.time()
# t = t2 - t1
# print("dataloadertime", t)
