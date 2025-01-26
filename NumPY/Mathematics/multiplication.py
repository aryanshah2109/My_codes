import numpy as np
# multiplication of array elements
arr1 = np.array([1,2,3,4,5,6])
product1 = np.prod(arr1)
print(product1)

# multiplication along axis of 2D array
arr2 = np.array([[1,2,3],
                 [4,5,6]])
product2 = np.prod(arr2,axis=0) # [4 10 18] axis = 0  means product across same column
                                # different rows
product3 = np.prod(arr2,axis=1) # [6 120] axis = 1 means product across same row different
                                # columns

print(product2)
print(product3)

# element wise multiplication of 2 arrays
arr3 = np.array([1,2,3])
arr4 = np.array([4,5,6])
product4 = np.multiply(arr3,arr4)       # same output as product4 = arr3 * arr4
print(product4)

# Dot product of 1D array
arr5 = np.array([1,2,3])
arr6 = np.array([10,11,12])
product5 = arr5 @ arr6      # same as product5 = np.dot(arr5,arr6)
print(product5)

# cross product of array
arr7 = np.array([[1,2],
                [3,4]])
arr8 = np.array([[7,8],
                [9,10]])
product6 = arr7 @ arr8      # same as product6 = np.dot(arr7,arr8)
print(product6)