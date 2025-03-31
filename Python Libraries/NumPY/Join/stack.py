import numpy as np
n1 = np.array([1,2,3,4])
n2 = np.array([5,6,7,8])
n3 = np.stack((n1,n2),axis=1)
print(n3)

n4 = np.array([[1,2,3,4],[5,6,7,8]])
n5 = np.array([[9,10,11,12],[13,14,15,16]])
n6 = np.stack((n4,n5),axis=1)
print(n6)