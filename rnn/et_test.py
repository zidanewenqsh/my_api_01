import torch
import torch.nn as nn

a = torch.randn(20,10)
b = torch.randn(10,1)
# a = torch.ones(20,10)
# b = torch.ones(10,1)
print(a@b)
print(torch.matmul(a,b))
print(0.5*10+0.5*(1+0.2*(-1.3)*0.4*2.7+0.4*7.4))