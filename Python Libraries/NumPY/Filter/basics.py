import numpy as np
n1 = np.array([4,2,1,9])
n2 = np.array([False,True,True,False])
n3 = n1[n2]     # filters the values where True is matched
print(n3)   

n4 = np.array([13,15,19,25])
emptyArray = []
for i in n4:
    if i > 14:
        emptyArray.append(True)
    else:
        emptyArray.append(False)
n5 = n4[emptyArray]
print(emptyArray)
print(n5)

# create a filter array that will return only even elements
n6 = np.array([1,4,2,3,9,11,43,24,19])
emptyArray2 = []
for i in n6:
    if i%2==0:
        emptyArray2.append(True)
    else:
        emptyArray2.append(False)
n7 = n6[emptyArray2]
print(emptyArray2)  # [False,True,True,False,False,False,False,True,False]
print(n7)           # [4,2,24]

# there is an alternate method too that does the same thing
n6 = np.array([1,4,2,3,9,11,43,24,19])
emptyArray2 = n6 % 2 == 0
n7 = n6[emptyArray2]
print(emptyArray2)  # [False,True,True,False,False,False,False,True,False]
print(n7)           # [4,2,24]