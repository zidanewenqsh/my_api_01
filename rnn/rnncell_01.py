import torch
import numpy as np

np.random.seed(12)
torch.random.manual_seed(12)
np.set_printoptions(precision=6, suppress=True)


class RNNCell:
    def __init__(self, weight_ih, weight_hh,
                 bias_ih, bias_hh):
        self.weight_ih = weight_ih
        self.weight_hh = weight_hh
        self.bias_ih = bias_ih
        self.bias_hh = bias_hh

        self.x_stack = []
        self.dx_list = []
        self.dw_ih_stack = []
        self.dw_hh_stack = []
        self.db_ih_stack = []
        self.db_hh_stack = []

        self.prev_hidden_stack = []
        self.next_hidden_stack = []

        # temporary cache
        self.prev_dh = None

    def __call__(self, x, prev_hidden):
        self.x_stack.append(x)
        print(x.shape,self.weight_ih.shape)
        # print(type(x),type(self.weight_ih)) (3, 4) (5, 4)
        next_h = np.tanh(
            np.dot(x, self.weight_ih.T)
            + np.dot(prev_hidden, self.weight_hh.T)
            + self.bias_ih + self.bias_hh) #(3, 5)
        # print(next_h.shape)

        self.prev_hidden_stack.append(prev_hidden)#(3, 5)
        # print(prev_hidden.shape)
        self.next_hidden_stack.append(next_h)
        # clean cache
        self.prev_dh = np.zeros(next_h.shape)
        return next_h

    def backward(self, dh):
        x = self.x_stack.pop()
        prev_hidden = self.prev_hidden_stack.pop()
        next_hidden = self.next_hidden_stack.pop()

        d_tanh = (dh + self.prev_dh) * (1 - next_hidden ** 2)
        self.prev_dh = np.dot(d_tanh, self.weight_hh)

        dx = np.dot(d_tanh, self.weight_ih)
        self.dx_list.insert(0, dx)

        dw_ih = np.dot(d_tanh.T, x)
        self.dw_ih_stack.append(dw_ih)

        dw_hh = np.dot(d_tanh.T, prev_hidden)
        self.dw_hh_stack.append(dw_hh)

        self.db_ih_stack.append(d_tanh)
        self.db_hh_stack.append(d_tanh)

        return self.dx_list


if __name__ == '__main__':
    rnn_cell_tensor = torch.nn.RNNCell(4, 5).double()
    print(rnn_cell_tensor.weight_ih.size())
    rnn_cell_numpy = RNNCell(
        rnn_cell_tensor.weight_ih.data.numpy(),
        rnn_cell_tensor.weight_hh.data.numpy(),
        rnn_cell_tensor.bias_ih.data.numpy(),
        rnn_cell_tensor.bias_hh.data.numpy())

    x_numpy = np.random.random((3, 4))
    x_tensor = torch.tensor(x_numpy, requires_grad=True)

    h_numpy = np.random.random((3, 5))
    h_tensor = torch.tensor(h_numpy, requires_grad=True)

    dh_numpy = np.random.random((3, 5))
    dh_tensor = torch.tensor(dh_numpy, requires_grad=True)

    next_h_numpy = rnn_cell_numpy(x_numpy, h_numpy)
    next_h_tensor = rnn_cell_tensor(x_tensor, h_tensor)

    rnn_cell_numpy.backward(dh_numpy)
    next_h_tensor.backward(dh_tensor)

    # print("numpy_hidden :\n", h_numpy)
    # print("tensor_hidden :\n", h_tensor.data.numpy())
    # print("------")
    #
    # print("dx_numpy :\n", np.array(rnn_cell_numpy.dx_list))
    # print("dx_tensor :\n", x_tensor.grad.data.numpy())
    # print("------")
    #
    # print("dw_ih_numpy :\n",
    #       np.sum(rnn_cell_numpy.dw_ih_stack, axis=0))
    # print("dw_ih_tensor :\n",
    #       rnn_cell_tensor.weight_ih.grad.data.numpy())
    # print("------")
    #
    # print("dw_hh_numpy :\n",
    #       np.sum(rnn_cell_numpy.dw_hh_stack, axis=0))
    # print("dw_hh_tensor :\n",
    #       rnn_cell_tensor.weight_hh.grad.data.numpy())
    # print("------")
    #
    # print("db_ih_numpy :\n",
    #       np.sum(rnn_cell_numpy.db_ih_stack, axis=(0, 1)))
    # print("db_hh_numpy :\n",
    #       np.sum(rnn_cell_numpy.db_hh_stack, axis=(0, 1)))
    # print("------")
    # print("db_ih_tensor :\n",
    #       rnn_cell_tensor.bias_ih.grad.data.numpy())
    # print("db_hh_tensor :\n",
    #       rnn_cell_tensor.bias_hh.grad.data.numpy())

    """
    代码输出
    numpy_hidden :
     [[ 0.944225  0.852736  0.002259  0.521226  0.552038]
     [ 0.485377  0.768134  0.160717  0.76456   0.02081 ]
     [ 0.13521   0.116273  0.309898  0.671453  0.47123 ]]
    tensor_hidden :
     [[ 0.944225  0.852736  0.002259  0.521226  0.552038]
     [ 0.485377  0.768134  0.160717  0.76456   0.02081 ]
     [ 0.13521   0.116273  0.309898  0.671453  0.47123 ]]
    ------
    dx_numpy :
     [[[ 0.234823  0.001947 -0.221488 -0.120629]
      [ 0.399758  0.061028 -0.244361 -0.42483 ]
      [ 0.28308   0.016405 -0.252444 -0.098564]]]
    dx_tensor :
     [[ 0.234823  0.001947 -0.221488 -0.120629]
     [ 0.399758  0.061028 -0.244361 -0.42483 ]
     [ 0.28308   0.016405 -0.252444 -0.098564]]
    ------
    dw_ih_numpy :
     [[ 0.778769  0.979517  0.700974  0.842186]
     [ 0.358268  1.077404  0.969949  0.37424 ]
     [ 0.540533  1.158021  0.862288  0.676237]
     [ 0.498534  1.444171  1.151646  0.643482]
     [ 0.507196  0.819969  0.791703  0.417976]]
    dw_ih_tensor :
     [[ 0.778769  0.979517  0.700974  0.842186]
     [ 0.358268  1.077404  0.969949  0.37424 ]
     [ 0.540533  1.158021  0.862288  0.676237]
     [ 0.498534  1.444171  1.151646  0.643482]
     [ 0.507196  0.819969  0.791703  0.417976]]
    ------
    dw_hh_numpy :
     [[ 0.992737  1.002905  0.267135  1.12167   0.760192]
     [ 0.748401  0.968729  0.24167   1.044483  0.325857]
     [ 1.044248  1.140167  0.234594  1.138324  0.622972]
     [ 1.174287  1.371561  0.27636   1.355196  0.591165]
     [ 0.566084  0.729519  0.260056  0.93798   0.346813]]
    dw_hh_tensor :
     [[ 0.992737  1.002905  0.267135  1.12167   0.760192]
     [ 0.748401  0.968729  0.24167   1.044483  0.325857]
     [ 1.044248  1.140167  0.234594  1.138324  0.622972]
     [ 1.174287  1.371561  0.27636   1.355196  0.591165]
     [ 0.566084  0.729519  0.260056  0.93798   0.346813]]
    ------
    db_ih_numpy :
     [ 1.798989  1.496149  1.77515   2.042895  1.345267]
    db_hh_numpy :
     [ 1.798989  1.496149  1.77515   2.042895  1.345267]
    ------
    db_ih_tensor :
     [ 1.798989  1.496149  1.77515   2.042895  1.345267]
    db_hh_tensor :
     [ 1.798989  1.496149  1.77515   2.042895  1.345267]
    """
