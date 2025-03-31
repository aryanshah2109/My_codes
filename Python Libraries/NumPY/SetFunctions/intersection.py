import numpy as np
n1 = np.array([10,20,30,40,50])
n2 = np.array([40,50,60,70])

n = np.intersect1d(n1,n2)
print(n)