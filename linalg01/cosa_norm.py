import numpy as np
from numpy import linalg

a = np.random.randn(3)
a_ = linalg.norm(a)
b = np.random.randn(3)
b_ = linalg.norm(b)
cosa = np.dot(a, b) / (a_ * b_)
print(cosa)
alpha = np.arccos(cosa) / np.pi
print(alpha)

a = np.random.randn(3, 4)
a_ = linalg.norm(a, axis=1, keepdims=True)

b = np.random.randn(3, 4)
b_ = linalg.norm(b, axis=1, keepdims=True)
print(a_, b_)
print(np.dot(a_, b_.T))
cosa = np.dot(a, b.T) / (np.dot(a_, b_.T))

print("cosa", cosa)
alpha = np.arccos(cosa)
print("alpha", alpha)
print("----------------------")

a = np.random.randn(3, 4)
a_ = a/linalg.norm(a, axis=1,ord=2, keepdims=True)

b = np.random.randn(3, 4)
b_ = b/linalg.norm(b, axis=1,ord=2, keepdims=True)
print(a_.shape,b_.shape)
# print("a",a_)
# print("b",b_)
# print(np.sqrt(np.sum(b_**2,axis=1)))
cosa = np.dot(a_, b_.T)

print("cosa", cosa)
alpha = np.arccos(cosa)
print("alpha", alpha)
print(alpha*180/np.pi)
