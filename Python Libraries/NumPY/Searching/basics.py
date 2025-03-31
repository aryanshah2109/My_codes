# np.where(array == elementToSearch)
# returns indices of occurance of element in a new array

import numpy as np
n1 = np.array([1,3,5,4,1,9,10,14,9,6,8,9])

n2 = np.where(n1 == 1)
print(n2)
n3 = np.where(n1 == 9)
print(n3)

N = np.where(n1==2)
print(N)

# find indices where elements are even
n4 = np.where(n1%2==0)
print(n4)

n5 = np.array([[1,4,3],[4,5,6]])
n6 = np.where(n5==4)
print(n6)