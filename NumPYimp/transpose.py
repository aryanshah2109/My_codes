import numpy as np
arr = np.array([[1,2],
                [4,5],
                [6,7]])
print(arr.transpose())
print(arr.ravel())  # flattens the array into 1D array

# difference between ravel() and reshape(-1)
# reshape(-1) always returns a view , it requires shape to fit
# ravel() returns view if possible else a copy, automatically handles memory layout