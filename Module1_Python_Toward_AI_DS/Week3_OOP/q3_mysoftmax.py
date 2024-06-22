import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / exp_x.sum(dim=0)


data = torch.Tensor([1, 2, 300000000])
my_softmax = MySoftmax()
output = my_softmax(data)
assert torch.isclose(round(output[0].item(), 2), 0.0, rtol=1e-09, atol=1e-09)
print(output)
