import os
import numpy as np

path = "./onet_07_4.pt"
# with open(path,encoding='unicode') as f:
#     print(f.readlines())
# print(chr(67))
# print(ord('C'),ord('O'),ord("N"), ord("S"))
# a = [1,2,3,4]
# print(min(a),max(a))
# a = np.random.randn(10,10)
# b = np.clip(a,-0.999,0.999)
# print(a)
# print(b)
# a = "aaa"
# # a = (1,2,3)
# # a = {0:1,1:2}
# # a = {1,2,3,4}
# print(a)
# b = np.array(list(a))
# print(b)
# print(type(a))
# a = np.array([1.22222222,2,3,4],dtype=np.str)
# print(a)
#
# a = [['a',1,2],['a',3,4],['b',4,5]]
# b = {}
# # b.update()
# for a1 in a:
#     if a1[0] in b.keys():
#         b[a1[0]].extend(a1[1:])
#     else:
#         # b[a1[0]]=[]
#         # b[a1[0]].extend(a1[1:])
#         b.update({a1[0]:a1[1:]})
# print(b)
a = [{0: [1, 2, 3]}, {1: [3, 4, 5]}]
b = {2: 'c'}
print(b.values())
for x in b.values():
    print(x)
a = np.array(a)

print(a)
print(b)
# print(*a.values())
print(*a)
c = map(lambda x: x.values(), list(a))
print(c)
# for x in c:
#     print(x)
# a = [[[1,2],[3,4]],[[5,6],[7,8]]]
# a = {0: [1, 2, 3], 1:[3, 4, 5]}
# # a = "123456"
# print(**a)
a = {1,2,3,4}
b = {3,4,5,6}
a = a.union(b)
print(a)
