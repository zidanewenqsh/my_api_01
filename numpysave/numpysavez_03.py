import numpy as np
import time
import pickle
import torch
import torch.nn as nn
from torch.utils import data

class Dataset(data.Dataset):
    def __init__(self, path):
        super(Dataset, self).__init__()
        # self.path = path
        # self.dataset = []
        for v in np.load(path).values():
            self.dataset = torch.from_numpy(v)

    def __len__(self):
        return len(self.dataset)
    def __getitem__(self, index):
        return self.dataset[index]


np.set_printoptions(precision=2, threshold=1000, suppress=True)

N, C, H, W = 100, 3, 416, 416
data_torch = torch.randn(N, C, H, W)

t1 = time.time()
np.savez("torch.npz", data_torch)

t2 = time.time()
t = t2 - t1
print("torchsavetime", t)

# t1 = time.time()
#
r = np.load("torch.npz")
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
dataset = Dataset("torch.npz")
print(type(dataset))
print(len(dataset))
t2 = time.time()
t = t2 - t1
print("datasettime", t)

t1 = time.time()
dataloader = data.DataLoader(dataset,10,True,drop_last=True)
print(len(dataloader))
for i,v in enumerate(dataloader):
    print(v.size(), type(v))
    break
t2 = time.time()
t = t2 - t1
print("dataloadertime", t)
