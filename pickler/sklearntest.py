# import sklearn
import torch
import torch.nn as nn
# from sklearn.externals import joblib
# from sklearn.externals import joblib
import joblib
# x = torch.randn(3,3)
# # 保存x
# joblib.dump(x, 'x.pkl')
# # 加载x
# x1 = joblib.load('x.pkl')
# print(x1)
layer = nn.Linear(3,2)
print(layer.parameters())
params = layer.parameters()

# 保存x
for p in params:
    print(p.size())
    joblib.dump(p, 'x.pkl')
# 加载x
x1 = joblib.load('x.pkl')
x2 = joblib.load('x.pkl')
print(x1)
print(x2)