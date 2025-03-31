import numpy as np
n1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
n2 = np.array([[10,11,12],[13,14,15],[16,17,18]])

n3 = n1.dot(n2)
n4 = n2.dot(n1)
print(n3)
print(n4)