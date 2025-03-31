# in copy, changes made to new array are not reflected in the original array
# in view, changes made to new array are reflected in the original array as well
# copies owns the data, and views does not own the data
import numpy as np
n1 = np.array([1,2,3,4,5])
n2 = n1.copy()
n2[1] = 10
print(n1)
print(n2)

n3 = np.array([1,2,3,4,5])
n4 = n3.view()
n4[1] = 10
print(n3)
print(n4)

# array.base return None for copy and the original array for view
print(n2.base)
print(n4.base)