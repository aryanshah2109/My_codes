# passing list and tuples to an array
import numpy as np

# array from a list
n1 = np.array([1,5,7,2,9])
print(n1)
print(type(n1))

# array from a tuple
n2 = np.array((3,4,5,1))
print(n2)
print(type(n2))

# if we have even one string in a list/tuple of integers/float, then all elements will become 
# a string

# if we have even boolean value in a list/tuple of integers/float, 
# then that will become 1 or 0

# if we have even one float in a list/tuple of integers, then all elements will become 
# a float
