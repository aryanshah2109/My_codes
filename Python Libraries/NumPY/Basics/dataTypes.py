'''
i = integer
b = boolean
u = unsigned integer
f = float
c = complex float
m = timedelta
M = datetime
O = object
S = string
U = unicode string
V = memory
'''

import numpy as np
n1 = np.array([1,2,3])
n2 = np.array(['apple','banana','orange'])
n3 = np.array([1.4,5.3,9.4])

print(n1.dtype)
print(n2.dtype)
print(n3.dtype)

n4 = np.array([1,2,3,4],dtype='S')
print(n4)
n5 = np.array(['1','4','9'],dtype = 'i')
print(n5)

n6 = np.array([1.1,2.3],dtype='i')
