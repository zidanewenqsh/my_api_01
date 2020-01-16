import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
print(s)
dates = pd.date_range('20130101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df)

print(df.mean())
print(df.mean(1))
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(1)
print(s)
print(df.sub(s, axis='index'))
print(df.apply(np.cumsum))

print(df.apply(lambda x: x.max() - x.min()))

s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())