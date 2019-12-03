import numpy as np
a = np.random.randn(3,3)
print(a)
b = a.astype("S10")
print(b)
'''
[[b'-0.2369307' b'1.27063002' b'1.05727708']
 [b'-0.0026401' b'-0.2105123' b'1.59293373']
 [b'-0.3469150' b'1.48631953' b'1.24069561']]'''
b = a.astype(np.str)
print(b)
'''
[['-0.2262423544549122' '-2.4911171449864935' '-0.5183012440574168']
 ['-1.383578898018582' '0.043446313146244316' '-0.30089351629825734']
 ['1.6895363138552841' '1.0428887775372717' '-0.13918185083772486']]'''