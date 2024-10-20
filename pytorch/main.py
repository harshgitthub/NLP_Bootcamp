import torch

x = torch.empty(3)
print(x)

y = torch.zeros(2,3)
print(y)

"""
the data types are int float denoted as torch.int , torch.float
"""


r = torch.tensor([2,3,56,7])
print(r)


t = torch.rand(2,3)
u = torch.rand(2,3)
torch.random.seed()

print(t)
print(u)

print(t+u)


# other  operations can be slicing , etc are also there 
# reshaping 

g = t.view(6,1)
print(g)

import numpy as np 

a = torch.ones(5)

#numpy array

p = a.numpy()

print(a)
print(p)

p[0] = 3
# here both of them changes together since they point to the same part of the memory  
# this happens only when this runs on the gpu 
print(a)
print(p)

o = torch.from_numpy(a)