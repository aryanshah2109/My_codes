import numpy as np

# np.array(list/tuple)
arr = np.array([1,2,3,4])
print(arr)
print(f"dimensions = {arr.ndim}")
print(f"shape = {arr.shape}")   # for 1D array, shape = (numOfElements, )

arr = np.array([[1,2,3,10],
                [4,5,6,11],
                [7,8,9,12]])
print(arr)
print(f"dimensions = {arr.ndim}")
print(f"shape = {arr.shape}")

# ndmin= num helps initialise with a given dimension
arr = np.array([1,2,3,4,5],ndmin=5)
print(arr)

# .shape returns number of element in each dimension and subdimensions

# np.zeros((shape))
arr = np.zeros((4,5))   # creates 2D array full of zeroes of given shape
print(arr)

# np.ones((shape))
arr = np.ones((3,5,4))  # creates 3D array full of zeroes of given shape
print(arr)

# np.full((shape),number)
arr = np.full((2,5),10)     # creates an array of given number and shape
print(arr)

# np.arange(low,high,step)
arr = np.arange(10,20,3)    # creates an array of elements in a range with a step
print(arr)                  # excluding high value

# np.random.rand(shape)
arr = np.random.rand(4,5)   # creates an array of given shape of floats [0,1) 
print(arr)                  # i.e. including 0 and excluding 1

# np.random.randint(low,high,size=numberOfIntegers)
arr = np.random.randint(10,30,size=10)  # creates array of given number of random 
print(arr)                              # integers in a given range 

# np.linspace(low,high,number)
arr = np.linspace(10,20,5)  # creates evenly spaced array from a range including
                            # the high value 
print(arr)

# identity matrix is one where only diagonal elements have element 1 and rest have 
# element 0 
# np.eye(N) creates an identity matrix of shape N x N
arr = np.eye(3)
print(arr)

# diagonal matrix is one where only diagonal elements are non zero
# rest all elements are zero
# np.diag([diagonal elements]) creates a diagonal matrix
arr = np.diag([1,2,3,4])
print(arr)

# np.diag(arr) returns an array of diagonal elements of the given array
arr = np.random.randint(10,20,size=16).reshape(4,4)
print(arr)
print(np.diag(arr))