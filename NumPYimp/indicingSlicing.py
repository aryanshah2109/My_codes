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

# boolean indexing -> filtering out elements for a condition
arr = np.random.randint(10,100,size=20).reshape((4,5))
print(arr)
print(arr[arr>50])
print(arr[(arr>50) & (arr%2==0)])      
# we use '&' instead of 'and' as we are using boolean conditions and in boolean
# conditions we use '&' instead of 'and'

# fancy indexing -> suppose from an 2D array of shape (4,5) we need row number
# 0 2 and 3 then we cannot do that by slicing as in slicing we only get continous 
# rows. So to fetch discontinuos rows, we use fancy indexing where a list of required
# rows is sent. the same can be done for cols
arr = np.random.randint(10,50,size=20).reshape((4,5))
print(arr)
print(arr[[0,2,3]])
print(arr[:,[0,2,3]])

# np.take(arr,[element1,element2,..]) flattens the given array and returns
# an array of the elements at given indices of the flattened array 
arr = np.array([[1, 2], [3, 4]])
taken = np.take(arr, [0,1,3])  # Takes elements at flattened indices
print("Taken elements:\n", taken)

# np.put(arr,[indiceToReplace],[newElements]) replaces the elements at given
# indice with the new elements
arr = np.array([[1,2,3],[4,5,6]])
np.put(arr,[1,4],[10,11])
print(arr)