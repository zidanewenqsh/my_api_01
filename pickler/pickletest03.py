import torch
import time
import pickle

# with open("a.data",'wb') as f:
#     for i in range(1000):
#         pickle.dump(torch.ones(500,500)*i, f)
datalist = []
t1 = time.time()
with open("a.data",'rb') as f:
    try:
        while True:
            datalist.append(pickle.load(f))
    except:
        print(1)
t2 = time.time()
print(t2-t1)
print(len(datalist))
a = float('-inf')
print(a)