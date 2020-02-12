import os
datalist = []
# 124.156.108.71	82	Guangxi Liuzhou
with open("ip.txt", "r") as f:
    for i,line in enumerate(f.readlines()):
        if i%2 ==0:
            datalist.append("{0}:{1}".format(line.split()[0], line.split()[1]))

with open("newip.txt",'w') as f:
    for x in datalist:
        print(x,file=f)

