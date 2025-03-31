import numpy as np

n = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(n.shape)
n1 = n.reshape(2,6)
print(n1)
print("Base: ",n1.base)
n2 = n.reshape(2,2,3)
print(n2)
print("Base: ",n2.base)
# after reshape, a view is created

# flattening the array means reshaping a multi dimensional array into a 1D array
# it can be done by array.reshape(-1)
n3 = np.array([[1,2,3],[4,5,6]])
n4 = n3.reshape(-1)
print(n4)

# flattening can also be done by functions like flatten, ravel
# rearranging of elements can be done by functions like rot90, flip, fliplr
# and flipud. They all come under advanced numpy



