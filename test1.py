import torch
N = 2
a = torch.arange(6).reshape((2,3))
b = torch.cat((a.repeat(1, N).view(N * N, -1), a.repeat(N, 1)), dim=1).view(N, -1, 2*3)
print(b)