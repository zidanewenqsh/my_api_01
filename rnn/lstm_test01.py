import torch
import torch.nn as nn
# rnn = nn.RNN(2,3,2)
num_layers = 1
batch_first = True
rnn = nn.LSTM(10, 20, num_layers, batch_first=batch_first)
for n,p in rnn.named_parameters():
    print(n)
    print(p.shape)
print("*************")

if batch_first:
    input = torch.randn(3, 5, 10)
else:
    input = torch.randn(5, 3, 10)

h0 = torch.randn(num_layers, 3, 20)
c0 = torch.randn(num_layers, 3, 20)
output, (hn,cn) = rnn(input, (h0,c0))
print(output.size())
print(hn.size(), cn.size())