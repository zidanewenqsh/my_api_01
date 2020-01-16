import torch.nn as nn
import torch
from torch.autograd import Variable

class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, cell_size, output_size):
        super(LSTM, self).__init__()
        self.hidden_size = hidden_size
        self.cell_size = cell_size
        self.gate = nn.Linear(input_size + hidden_size, cell_size)
        self.output = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
        self.tanh = nn.Tanh()
        self.softmax = nn.LogSoftmax()

    def forward(self, input, hidden, cell):
        combined = torch.cat((input, hidden), 1)
        f_gate = self.gate(combined)
        i_gate = self.gate(combined)
        o_gate = self.gate(combined)
        f_gate = self.sigmoid(f_gate)
        i_gate = self.sigmoid(i_gate)
        o_gate = self.sigmoid(o_gate)
        cell_helper = self.gate(combined)
        cell_helper = self.tanh(cell_helper)
        cell = torch.add(torch.mul(cell, f_gate), torch.mul(cell_helper, i_gate))
        hidden = torch.mul(self.tanh(cell), o_gate)
        output = self.output(hidden)
        output = self.softmax(output)
        return output, hidden, cell

    def initHidden(self):
        return Variable(torch.zeros(1, self.hidden_size))

    def initCell(self):
        return Variable(torch.zeros(1, self.cell_size))

if __name__ == '__main__':
    lstm = nn.LSTM(10,20,2,batch_first=True)
    input = torch.randn(5,3,10)
    # h0 = torch.zeros(2,3,20)
    h0 = torch.zeros(2,5,20)
    c0 = torch.zeros(2,5,20)
    print(h0.size())
    output,(hn,cn) = lstm(input,(h0,c0))
    # output, (hn, cn) = lstm(input)
    print(output.size())
    print("input",input.size())
    print("hidden",h0.size())
    print("cell",c0.size())
