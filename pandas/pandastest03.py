import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10, 4))
print(df)

pieces = [df[:3], df[3:7], df[7:]]
print(pieces)
print(pd.concat(pieces))

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1,2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))

left = pd.DataFrame({'key': ['foo', 'bar', 'foo1', 'bar1'], 'lval': [1,2,3,4]})
right = pd.DataFrame({'key': ['foo', 'bar','foo2', 'bar2'], 'rval': [5,6,7,8]})
print("left")
print(left)
print("right")
print(right)
print(pd.merge(left, right, on='key'))
print(pd.merge(left, right, on='key',how="left"))
print(pd.merge(left, right, on='key',how="right"))
print(pd.merge(left, right, on='key',how="outer"))
exit()
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
print(df)
s = df.iloc[3]
print(df.append(s, ignore_index=True))
# print(df)