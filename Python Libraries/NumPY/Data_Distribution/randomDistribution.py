# generate a 1D array of size 10 having elements 1,2,4,5 in random
# probability of occurance of 1 is 0.2
# probability of occurance of 2 is 0.1
# probability of occurance of 4 is 0.5
# probability of occurance of 5 is 0.2

import numpy as np
n = np.random.choice([1,2,4,5],p=[0.2, 0.1, 0.5, 0.2], size=(100))
print(n)

n1 = np.random.choice([1,2,4,5], p=[0.2,0.1,0.5,0.2], size=(100,3))
print(n1)