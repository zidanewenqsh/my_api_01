import torch
import json
a = torch.randn(3,3)
b = torch.randn(5,5)
# with open("a.json",'w',encoding='utf-8') as f:
#     json.dump(a,f)
#     json.dump(b,f)
"TypeError: Object of type Tensor is not JSON serializable"