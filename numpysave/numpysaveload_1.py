import numpy as np
import time
import pickle
import torch
import torch.nn as nn
from torch.utils import data
import os
'''
np.save
np.load
变量一个一个的存，一个一个的取
用这个存torch数据容易死机
'''
a = np.arange(8)
b = np.add.accumulate(a)
c = a + b
# f = open("result.npy", "wb")
# np.save(f, a) # 顺序将a,b,c保存进文件对对象f
# np.save(f, b)
# np.save(f, c)
# f.close()
f = open("result.npy", "rb")
print(np.load(f)) # 顺序从文件对象f中读取内容
# array([0, 1, 2, 3, 4, 5, 6, 7])
print(np.load(f))
# array([ 0, 1, 3, 6, 10, 15, 21, 28])
print(np.load(f))
# array([ 0, 2, 5, 9, 14, 20, 27, 35])
f.close()



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


class SaveDataset:
    def __init__(self, datas, savedir):
        self.datas = datas
        self.savedir = savedir

    def save(self):
        for i, data_ in enumerate(self.datas):
            savename = "data_{0}.npy".format(i)
            savepath = os.path.join(self.savedir,savename)
            with open(savepath,'wb') as f1:
                np.save(f1, data_)
if __name__ == '__main__':
    savedir = "../saves/a"
    datas = torch.randn(10,3,416,416)
    savedataset = SaveDataset(datas,savedir)
    # savedataset.save()





np.set_printoptions(precision=2, threshold=1000, suppress=True)

N, C, H, W = 10000, 3, 416, 416
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

# t1 = time.time()
# dataset = Dataset("torch.npz")
# print(type(dataset))
# print(len(dataset))
# t2 = time.time()
# t = t2 - t1
# print("datasettime", t)
#
# t1 = time.time()
# dataloader = data.DataLoader(dataset,10,True,drop_last=True)
# print(len(dataloader))
# for i,v in enumerate(dataloader):
#     print(v.size(), type(v))
#     break
# t2 = time.time()
# t = t2 - t1
# print("dataloadertime", t)
