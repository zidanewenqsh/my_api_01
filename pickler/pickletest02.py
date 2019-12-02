import pickle


d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
with open('dump.txt', 'wb') as f:
    pickle.dumps(d, f)#TypeError: an integer is required (got type _io.BufferedWriter)
    pickle.dump(d, f)
with open('dump.txt', 'rb') as f:
    d1 = pickle.load(f)
print(d1)


