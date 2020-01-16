import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz''foo', 'foo', 'qux', 'qux'],
['one', 'two', 'one', 'two',
'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print(index)
df = pd.DataFrame(np.random.randn(7, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
print(df2)
# print(df)
stacked = df2.stack()
print(stacked)
print(stacked.unstack())
print(stacked.unstack(1))
print(stacked.unstack(0))