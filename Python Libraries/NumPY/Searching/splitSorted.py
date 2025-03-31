# numpy.searchsorted() is a function in NumPy used to find indices where elements should # be inserted in a sorted array to maintain its order. 

import numpy as np
n1 = np.array([1,3,5,9,12,19,45])
print(np.size(n1))
n2 = np.searchsorted(n1,5)
print(n2)

# it returns the index where the element should be added in the array

# if we want to search from the right, we add the side = 'right' parameter
# When using the side='right' parameter, the function looks for the first position after # the last occurrence of the target element. It essentially returns the index where the  # target element could be inserted on the right to maintain the sorted order.
n3 = np.searchsorted(n1,12,side='right')
print(n3)