import torch
import torch.nn as nn
gru = nn.GRU(2,3,2)
a = torch.randn(5,5,2)
h0 = torch.zeros(2,5,3)

print(a)
for i,p1 in enumerate(gru.parameters()):
    nn.init.constant_(p1,i)
    print(i)
for n,p in gru.named_parameters():
    print(n)
    print(p.size())
    # print(p)
b, hn = gru(a,h0)
print(b)
print(b.size())