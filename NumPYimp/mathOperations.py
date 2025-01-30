import numpy as np
arr = np.random.randint(1,20,size=10)
print(arr)
# scaler operations on each element of the array
arr = arr + 1
print(arr)
arr = arr - 1
print(arr)
arr = arr * 2
print(arr)
arr = arr / 2
print(arr)

arr1 = np.array([1,2,3,4])
arr2 = np.array([10,11,12,13])

# operations on 2 arrays
print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.divide(arr1,arr2))

# np.power(arr,power) raises power of each element to given power
arr = np.array([1,2,3,4,5,6,7])
print(np.power(arr,2))

# np.sqrt(arr) gives square root of each element
arr = np.array([100,200,300,400,500,600,700])
print(np.sqrt(arr))

# for 1D arrays, np.dot() returns the sum of products of each term
# for 1D arrays, np.dot() and np.matmul() return the same thing
arr3 = np.array([1,2,3,4])      
arr4 = np.array([10,11,12,13])
print(np.dot(arr3,arr4))
print(np.matmul(arr3,arr4))


# for 2D arrays, np.dot(), arr1 @ arr2, np.matmul() return the same thing 
# i.e. the matrix product
arr1 = np.array([[1,2,3,4],[5,6,7,8]])
arr2 = np.array([[10,11],[12,13],[14,15],[16,17]])

print(np.dot(arr1,arr2))
print(np.matmul(arr1,arr2))
print(arr1 @ arr2)

# np.prod(arr,axis) gives product of elements of multidimensional arrays among its 
# rows(axis=0) or columns(axis=1)
arr1 = np.array([[1,2,3,4],
                 [5,6,7,8]])
print(np.prod(arr1,axis=0)) # row
print(np.prod(arr1,axis=1)) # col