import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
# df = pd.DataFrame(np.random.randn(6,4), index=np.arange(6), columns=[1,2,3,4])
print(df)

# 删除数据
# df = df.drop([3],axis=0)
# print(df)

# exit()
df2 = pd.DataFrame({ 'A' : 1., 'B' : pd.Timestamp('20130102'),'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
 'D' : np.array([3] * 4,dtype='int32'), 'E' : pd.Categorical(["test","train","test","train"]),'F' : 'foo' })
print(df2)
print(df2.dtypes)
print(df.head(2))
print(df.tail(2))
print(df.index)
print(df.columns)

print(df.values)
# exit()
print(df.describe())
print(df.T)

print(df.sort_index(axis=0, ascending=False))

print(df.sort_values(by='B'))

print("***********************")

print(df['D'])
print(df[0:3])
# print(df['2013-01-02'])#KeyError: '2013-01-02'
print("***********************++++++++++++++")
# print(df['2013-01-02'])
print(df['2013-01-02':"2013-01-03"])
print(df.loc['2013-01-02','A'])
print(df.iloc[1,2])
print(df.A) # 英文列名可以这么引用

exit()
# print(df['A':'C']) #ValueError: Given date string not likely a datetime.
print(df.loc[dates[0]])
print(df.loc[:,['A','B']])

exit()
print(df.loc['20130102':'20130104',['A','C']])
print("***********************")
print(df.loc['20130102',['A','B']])
print(df.loc[dates[0],'A'])
print(df.at[dates[0],'A'])
print(df.iloc[3])
print(df.iloc[3:5,0:2])
print(df.iloc[[1,2,4],[0,2]])
print(df.iloc[1:3,:])
print(df.iloc[:,1:3])
print(df.iloc[1,1])
print(df.iat[1,1])
print("***********************")
print(df[df.A > 0])
print(df[df > 0])
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
print(df2)
print(df2[df2['E'].isin(['two','four'])])

print("***********************")
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101', periods=6))
print(s1)
df['F'] = s1
print(df)
df.at[dates[0],'A'] = 0
df.iat[0,1] = 0
print(df)
print(len(df))
df.loc[:,'D'] = np.array([5] * len(df))
# df.loc[:,'D'] = np.array([1,2,3,4,5]).reshape(-1,1)
print(df)
print("***********************")
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
print(df1)
df1.loc[dates[0]:dates[1],'E'] = 1
print(df1)

print(df1.dropna(how='any'))
print(df1.fillna(value=5))
print(pd.isnull(df1))