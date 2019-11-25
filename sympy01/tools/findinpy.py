import os
#coding:utf8
import os

#获取当前目录绝对路径
dir_path = os.path.dirname(os.path.abspath(__file__))
print('当前目录绝对路径:',dir_path)


#获取上级目录绝对路径
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('上级目录绝对路径:',dir_path)

# searchpath = r"D:\PycharmProjects"
searchpath = r"D:\PycharmProjects\my_api_01\sympy01"

searchword = "summation"


for root,dirs,files in os.walk(searchpath):
    for file in files:
        file_ = os.path.join(root,file)
        # print(file_, os.path.exists(file_))
        if file_.endswith("py"):
            with open(file_, 'r', encoding='utf-8') as f:
                try:
                    data_ = f.read()
                    if searchword in data_:
                        print(file_)
                except BaseException as e:
                    print(e)
                    print("error",file_)
