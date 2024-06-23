import torch
import torch.nn as nn
import torch.nn.functional as F


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        return F.softmax(x, dim=0)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        x_max = torch.max(x)
        x_exp = torch.exp(x - x_max)
        return x_exp / torch.sum(x_exp)


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)

data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)
