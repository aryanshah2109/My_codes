# n[start:end:jump]
import numpy as np
n = np.array([1,2,3,4,5,6,7,8])
print(n[1:3])
print(n[:4])
print(n[5:])
print(n[2:5:2])

n2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(n2[:,2:])     # prints [[3,4,5] , 
                    #          [7,8,9]]
print(n2[:,::2])    # prints [[1,3,5],
                    #          [6,8,10]]
