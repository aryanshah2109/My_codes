# in copy, changes made to new array are not reflected in the original array
# in view, changes made to new array are reflected in the original array as well
# copies owns the data, and views does not own the data

# arr.base returns None for copy and the original array for view
# create a copy by arr2 = arr1.copy()
# create a view by arr2 = arr1.view()

import numpy as np
arr1 = np.array([1,2,3])
print(arr1)

arr2 = arr1.copy()
print(arr2)
print(arr2.base)

arr2 = arr1.view()
print(arr2)
print(arr2.base)