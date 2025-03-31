# can be done by array_split()
import numpy as np
n1 = np.array([1,2,3,4,5,6,7,8,9])
n2 = np.array_split(n1,3)
print(n2)
print(n2[0])
print(n2[1])
print(n2[2])

n3 = np.array_split(n1,6)
print(n3)

# 2d arrays
print("\n2D arrays::")
n4 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
n5 = np.array_split(n4,3)
print(n5)

# axis =1 splits along rows
# ie. n6 = [1,4,7,10,13,16] , [2,5,8,11,14,17] , [3,6,9,12,15,18]
n6 = np.array_split(n4,3,axis=1)
print(n6)
for i in n6:
    print(i)