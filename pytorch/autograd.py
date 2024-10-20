# autograd package is used to create / calculate gradients and other things 

import torch 
torch.random.seed()

X = torch.randn(3,requires_grad=True)
y = X+2
print(y)

z = y*y*2
print(z)

v = torch.tensor([0.1,1.0,0.001] , dtype=torch.float32)
z.backward(v)  # dz/dx

print(X.grad)

# to prevent the tracking of the gradient 
"""
x.detach()
x.requires_grad_(False)
with torch.no_grad()
"""

# note a trailing _ indicates it will make changes inplace 

weights = torch.ones(4,requires_grad=True)

optimiser = torch.optim.SGD(weights, lr=0.1)
optimiser.step()
optimiser.zero_grad() # this resets the gradients back to the original value 