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
torch保存的文件太大
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



# class Dataset(data.Dataset):
#     def __init__(self, path):
#         super(Dataset, self).__init__()
#         # self.path = path
#         # self.dataset = []
#         for v in torch.load(path).values():
#             self.dataset = torch.from_numpy(v)
#
#     def __len__(self):
#         return len(self.dataset)
#     def __getitem__(self, index):
#         return self.dataset[index]


class SaveDataset:
    def __init__(self, datas, savedir):
        self.datas = datas
        self.savedir = savedir

    def save(self):
        for i, data_ in enumerate(self.datas):
            savename = "data_{0}.torch".format(i)
            savepath = os.path.join(self.savedir,savename)
            # with open(savepath,'w') as f1:
            torch.save(data_, savepath)

if __name__ == '__main__':
    savedir = "../saves/a"
    datas = torch.randn(10,3,416,416)
    # savedataset = SaveDataset(datas,savedir)
    t1 = time.time()
    # savedataset.save()
    t2 = time.time()-t1
    print("savetime",t2)
    path1 = os.path.join(savedir,"summ.torch")
    datas1 = torch.randn(100,3,416,416)
    # torch.save(datas1,path1)
    a = torch.load(path1)
    print(a)