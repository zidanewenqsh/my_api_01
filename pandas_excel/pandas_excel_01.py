import numpy as np
from numpy import nan as NAN
import pandas as pd
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
# 处理info表中的重复值，以'a'为唯一去重，保留重复值第一行
info = info.drop_duplicates(['a'],keep='first')
# 缺失值处理
# 用列的平均值填充
# info = info.fillna(info.mean())
# 用常数填充
info = info.fillna(0)
print(info.head(6))
print(info)
# 将info表和degree表合并
# m1 = pd.merge(degree, info, on='a', suffixes=['_info','_degree'])
m1 = pd.merge(degree, info, on='a') #  a  b_x  c_x  b_y  c_y

# 删除"b"列
m1 = m1.drop(['b_x'], axis=1)
# 普通单列排序，按照"a"排序
#ascending表示降序或升序
#method 可选择dense\first\min\max
# m1['sort_num']=m1['a'].rank(asc)

print(m1)
print(m1.shape)