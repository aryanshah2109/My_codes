import numpy as np
n1 = np.array([10,20,30,40,50,60,70])
n2 = np.array([50,60,70,80,90,100])

n3 = np.setdiff1d(n1,n2)
print(n3)

n4 = np.setdiff1d(n2,n1)
print(n4)