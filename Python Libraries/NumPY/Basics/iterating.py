import numpy as np
# iterating through an 1D array

n1 = np.array([1,2,3,4,5,6,7,8,9])
for i in n1:
    print(i,end=" ")
print('\n')
# iterating through an 2D array
n2 = np.array([[1,2,3,4],[5,6,7,8]])    

# iterating each row in a 2D
for i in n2:    
    print(i)

# iterating each element in a 2D
for i in n2:
    for j in i:
        print(j,end=" ")
    print(" ")

print("3D")
# Iterating through a 3D
n3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in n3:
    for j in i:
        for k in j:
            print(k)

# nditer()
# we use nditer() for iterating through a very complex array
n4 = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for i in np.nditer(n4):
    print(i)

n5 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
for i in np.nditer(n5[:,::2]):
    print(i)