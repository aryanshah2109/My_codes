import numpy as np

# vectors are 1D arrays
v1 = np.array([1,2,3])
v2 = np.array([5,6,-1])

# addition and subtraction of vectors
print(v1+v2)
print(v1-v2)

# scalar multiplication of vector
print(4*v1)

# norm of a vector = length of the vector
print(np.linalg.norm(v1))

# dot product
print(np.dot(v1,v2))