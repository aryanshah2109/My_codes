import numpy as np

# arr.shape = returns dimensions as tuples
arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(arr)
print(arr.shape)

# arr.reshape(shape) = converts the original array to new shape
# arr.reshape(-1) = converts multidimensional array to 1D array

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr = arr.reshape(3,4)
print(arr)
print(arr.ndim)

arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
arr = arr.reshape(-1)
print(arr)
print(arr.ndim)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(-1,1))    # -1 indicates take all elements
print(arr.reshape(1,-1))    

# np.expand_dims(arr,axis=) adds an extra dimension
# axis=0 rows, axis=1 colums
arr = np.array([[1,2,3],
                [4,5,6]])
print(np.expand_dims(arr,axis=0),arr.shape)

print(np.expand_dims(arr,axis=1),arr.shape)
