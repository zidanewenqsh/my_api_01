import torch
import torch.nn as nn
rnn = nn.RNN(10,4,1)
a = torch.randn(5,3,10)
b, h = rnn(a)
print(b.size())
for n,p in rnn.named_parameters():
    print(n)
    print(p.size())