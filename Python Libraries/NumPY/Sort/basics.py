import numpy as np
n1 = np.array([13,43,5,2,1,5,1,9,13])
n2 = np.sort(n1)
print(n2)

n3 = np.array([[5,3,4],[1,9,2]])
n4 = np.sort(n3)
print(n4)

n5 = np.array([[[10,2],[11,1],[42,9],[8,10]]])
n6 = np.sort(n5)
print(n6)

# it creates a new array like copy
# so it doesnt affect the original array

n7 = np.array(['apple','orange','banana'])
print(np.sort(n7))