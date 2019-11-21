import numpy as np
a = np.array([3**(0.5)/2,1])
fai = np.pi/6
m = np.array([np.cos(fai),np.sin(fai),-np.sin(fai),np.cos(fai)]).reshape(2,2)
print(a)
print(m)