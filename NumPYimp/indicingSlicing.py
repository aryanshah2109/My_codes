import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
for i in arr:
    print(i,end=" ")
print("\n")
# np.nditer(arr) -> helps iterate through a multidimesional array without using 
# multiple nested loops
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in np.nditer(arr):
    print(i)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
print(arr[:])   # prints all elements
print(arr[:4])  # prints from 0 to given indice -1
print(arr[2:])  # prints from indice 2 to end
print(arr[2:5]) # print for indice 2,3,4
print(arr[2:7:2])

print("\n")
arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]])
print(arr[:])   # prints all elements
print(arr[:,2:4])  # [[3,4],[9,10],[15,16]]
# the first part means include all elements
# the second part means include elements at indice 2,3 for each element
