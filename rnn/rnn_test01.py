import torch
import torch.nn as nn
# rnn = nn.RNN(2,3,2)
num_layers = 1
rnn = nn.RNN(10, 20, num_layers)
for n,p in rnn.named_parameters():
    print(n)
    print(p.shape)
print("*************")
input = torch.randn(5, 3, 10)
h0 = torch.randn(num_layers, 3, 20)
output, hn = rnn(input, h0)
print(output.size())
print(hn.size())