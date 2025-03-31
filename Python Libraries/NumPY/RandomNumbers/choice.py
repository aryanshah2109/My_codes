# chooses random value from an array
import numpy as np
n = np.array([3,5,1,4,5,10,7,8,11])
n2 = np.random.choice(n)
print(n2)

# getting a 2D array from a 1D array where elements of 1D are chosen in random order
n3 = np.random.choice([3,5,1,4,5,10,7,8,11],size=(4,6))
print(n3)
