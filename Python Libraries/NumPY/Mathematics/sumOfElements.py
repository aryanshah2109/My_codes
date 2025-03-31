# returns the sum of the matrix elements
import numpy as np

n1 = np.array([1,2,3])
n2 = np.array([4,5,6])

n3 = np.sum([n1,n2])
print(n3)    

n4 = np.sum([n1,n2],axis=0)     # sum along the columns elements
print(n4)

n5 = np.sum((n1,n2),axis=1)     # sum along the rows elements
print(n5)

