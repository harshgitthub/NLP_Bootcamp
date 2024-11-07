from transformers import pipeline 

import torch 

classifier  = pipeline("sentiment-analysis")
res = classifier('i have been waiting for you')
print(res)
