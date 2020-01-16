import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],'C' : np.random.randn(8),
'D' : np.random.randn(8)})
print(df)
print(df.groupby('A').sum())
print(df.groupby(['A','B']).sum())