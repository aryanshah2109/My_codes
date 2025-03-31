# shape indicates the number of rows and columns in a matrix

import numpy as np
n = np.array([[1,3],[6,8],[2,5]])
print(n.shape)  # prints rows and columns

# changing the shape of a matrix
n.shape = (2,3)
print(n.shape)
print(n)