# it is a property of numpy where the dimension of an array is changed implicitely 
# while performing any operation on it
import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])  # shape = (2,3)
arr2 = np.array([1,2,3])            # shape = (3,)
print(arr1+arr2)                    # shape = (2,3)
# Here the 1D was changed into 2D by broadcasting
# arr2 initailly was [1,2,3]
# after broadcasting, it is now [[1,2,3],
#                                [1,2,3]]
# Hence the column was stretched with the same elements

'''
When performing operations between arrays, NumPy follows these rules:
1) Compare shapes from right to left.
2) If dimensions match, they are compatible.
3) If one of the dimensions is 1, it is "stretched" to match the other.
4) If neither dimension is 1 and they don't match, broadcasting fails.

'''