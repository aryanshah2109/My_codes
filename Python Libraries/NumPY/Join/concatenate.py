import numpy as np
n1 = np.array([1,2,3,4])
n2 = np.array([5,6,7,8])
n3 = np.concatenate((n1,n2))
print(n3)

# concatenate 2 2D arrays based on rows (axis=1)
n3 = np.array([[1,2],[3,4]])
n4 = np.array([[5,6],[7,8]])
n5 = np.concatenate((n3,n4),axis=1)
print(n5)

# concatenate 2 2D arrays based on columsn(axis = 0)
n6 = np.concatenate((n3,n4),axis=0)
print(n6)