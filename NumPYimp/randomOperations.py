import numpy as np
import random

# np.random.shuffle(arr) shuffles the array elements i.e arranges them in random
# order. This modifies the original array

arr = np.array([1,2,3,4,5])
np.random.shuffle(arr)
print(arr)

# np.random.permutation(arr) does the same thing as shuffle but doesnt make changes
# to original array. It creates a new array

print(np.random.permutation(arr))
print(arr)

# np.random.choice(arr,numOfChoice) chooses random values from the array
arr = np.random.randint(1,100,10)
print(arr)
print(np.random.choice(arr,4))

# np.random.uniform(low,high,size) generates floating numbers evenly 
# distributed over a given range
low = 1
high = 10
size = 5
print(np.random.uniform(low,high,size))

# np.random.seed() ensures the same numbers are chosen in the next random codes
# in every output
# 42 is a conventional number you can also use 10 or any other number

np.random.seed(42)
print(np.random.rand(5))