import torch
import pickle
import torch.nn as nn
from torch.nn import init

a = torch.randn(1000,1000)
b = torch.randn(1000,1000)
layer = nn.Linear(3,2)
param = layer.parameters()
layer1 = nn.Linear(3,2)

with open("a.data",'wb') as f:
    pickle.dump(a,f)
    pickle.dump(b,f)
    # for p in param:
    #     print(p)
    #     pickle.dump(p,f)
# layer1_dict = layer1.state_dict()
# print(type(layer1_dict))
with open("a.data",'rb') as f:
    # print(pickle.load())
    a1 = pickle.load(f)
    b1 = pickle.load(f)
    # layer1.weight = pickle.load(f)
    # layer1.bias = pickle.load(f)
    # for k,v in layer1.state_dict().items():
        # print(k)
        # print(v)
        # print(layer1_dict[k])
        # layer1_dict[k] = pickle.load(f)
    # for p1 in layer1.parameters():
    #     p2 = pickle.load(f)
    #     # print(p1)
    #     p1 = nn.Parameter(p2)
    #     print(p1)

#
# for p1 in layer1.parameters():
#     print(p1)
# print(a1)
# print(b1)