import numpy as np

m1 = np.array([[1,2,3],[4,5,6]])
m2 = np.array([[6,-2,0],[3,9,-6]])

# addition subtraction
print(np.add(m1,m2))
print(np.subtract(m1,m2))

# product
m3 = np.array([[6,-2],[2,6],[9,1]])
print(np.dot(m1,m3))

# determinant
m4 = np.array([[6,1],[5,6]])
print(np.linalg.det(m4))

# inverse
print(np.linalg.inv(m4))