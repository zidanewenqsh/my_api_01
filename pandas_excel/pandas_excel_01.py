import numpy as np
from numpy import nan as NAN
import pandas as pd
import matplotlib.pyplot as plt
# from pandas import Series, DataFrame
exl_file = r"./testdata.xlsx"
exl = pd.ExcelFile(exl_file)
print(exl.sheet_names,len(exl.sheet_names))
info = pd.read_excel(exl_file,sheet_name='info')
print(info.head(4))
print(info.shape)
degree = pd.read_excel(exl_file,sheet_name="degree")
print(degree.head(4))
print(degree.shape)
print("********")
print(degree)
print("********")
# 处理info表中的重复值，以'a'为唯一去重，保留重复值第一行
# info = info.drop_duplicates(['a'],keep='first')
# 缺失值处理
# 用列的平均值填充
# info = info.fillna(info.mean())
# 用常数填充
info = info.fillna(0)
print(info.head(6))
print(info)
# exit()
# 将info表和degree表合并
# m1 = pd.merge(degree, info, on='a', suffixes=['_info','_degree'])
m1 = pd.merge(degree, info,how="outer", on='a') #  a  b_x  c_x  b_y  c_y
# how="inner", "left", "right", "outer"
# a列不要有重复的数据，否则不对

# m1 = pd.merge(degree, info)
print("****************")
print(m1)
print("****************")
exit()
# exit()
# 删除"b"列
m1 = m1.drop(['b'], axis=1)
# 普通单列排序，按照"a"排序
#ascending表示降序或升序
#method 可选择dense\first\min\max
# m1['sort_num']=m1['a'].rank(asc)

print(m1)
print(m1.shape)
print(m1.index)
print(m1.columns)
print(m1.values)
# exit()
i = m1.index
v = m1.values
print(v[:,1])
print(type(v),v.dtype)
a = np.array([1,2,3]).astype('f4')
print(a)
print(m1.describe())
plt.plot(i,v[:,1:])
plt.show()
plt.pause(0.1)