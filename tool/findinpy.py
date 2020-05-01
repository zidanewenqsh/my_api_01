import os
#coding:utf8
import os
import time
#获取当前目录绝对路径
dir_path = os.path.dirname(os.path.abspath(__file__))
print('当前目录绝对路径:',dir_path)


#获取上级目录绝对路径
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('上级目录绝对路径:',dir_path)

# searchpath = r"D:\PycharmProjects"
# searchpath = r"H:\python程序备份2019\PycharmProjects"
searchpath = r"D:\PycharmProjects"
# searchpath = r'G:\liev备份\PycharmProjects'
searchword = "init.constant_"
# self.optimizer = optim.Adam([{'params': self.encoder.parameters()}, {'params': self.decoder.parameters()}])

for root,dirs,files in os.walk(searchpath):
    for file in files:
        file_ = os.path.join(root,file)
        # print(file_, os.path.exists(file_))
        if file_.endswith("py"):
            with open(file_, 'r', encoding='utf-8') as f:
                try:
                    data_ = f.read()
                    if searchword in data_:
                        print(file_,time.strftime("%Y%m%d%H%M%S",time.localtime(os.path.getmtime(file_))))
                    f.seek(0,0)
                    data_1 = f.readlines()
                    # f.seek(0,0)
                    for d1 in data_1:
                        if searchword in d1:
                            print("fileis",file_)
                            print(d1.strip())

                except BaseException as e:
                    # print(e)
                    # print("error",file_)
                    pass
