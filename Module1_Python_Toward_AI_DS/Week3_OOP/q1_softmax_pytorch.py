import torch
import torch.nn as nn

data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
assert torch.isclose(round(output[0].item(), 2), 0.09, rtol=1e-09, atol=1e-09)
print(output)
