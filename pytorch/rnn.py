import torch
import torch.nn as nn 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 


class RNN(nn.Module):
    # nn.RNN 
    def __init__(self , input_size , hidden_size , output_size):
        super(RNN , self).__init__()

        self.hidden_size = hidden_size
        self.i2h = nn.Linear(input_size + hidden_size , hidden_size)
        self.i2o = nn.Linear(input_size+hidden_size , output_size)
        self.softmax = nn.LogSoftmax(dim = 1)


    def forward(self , input_tensor , hidden_tensor):
        combined = torch.cat((input_tensor, hidden_tensor),1)

        hidden = self.i2h(combined)
        output = self.i2o(combined)

        output = self.softmax(output)
        return output , hidden 

    def init_hidden(self):
        return torch.zeros(1,self.hidden_size)

