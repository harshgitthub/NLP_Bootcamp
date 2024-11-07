import torch 
import numpy as np 
import torch.nn as nn 

# x = np.array([1,2,3,4] , dtype=np.float32)
# y = np.array([2,4,6,8] , dtype=np.float32)

x = torch.tensor([1,2,3,4] , dtype=torch.float32)
y = torch.tensor([2,4,6,8] , dtype=torch.float32)

model = nn.Linear()

w = torch.tensor(0.0 , dtype=torch.float32 , requires_grad = True )
def forward(x):
    return w*x

# def loss(y , y_pred):
#     return ((y_pred-y)**2).mean()

# gradient 
# MSE = 1/N *(w*x -y)**2
# d/dx = 1/N 2x(w*x -y)

def gradient(x,y,y_pred):
    return np.dot(2*x , y_pred- y).mean()

print(f'Prediction before training : f(5) = {forward(5):.3f}')

# training 
learning_rate = 0.01
n_iters = 10 
loss = nn.MSELoss()
optimizer = torch.optim.SGD([w] , learning_rate)

for epoch in range(n_iters):
    y_pred = forward(x)

    # loss
    l = loss(y , y_pred)

    # gradients 
    # dw = gradient(x,y,y_pred)
    l.backward()

    # update weights 
    # w-= learning_rate*dw
    # now we can do 
    optimizer.step()

    #zero gradients 
    optimizer.zero_grad()

    if epoch % 1 == 0 :
        print(f'{epoch+1} : w = {w:.3f} , loss = {l:.8f}')


print(f'Prediction after training : f(5) = {forward(5):.3f}')
