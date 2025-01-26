# 1D, 2D and 3D arrays
import numpy as np

# 0D array
n0 = np.array(3)
print(n0)
print(f"Dimensions are {n0.ndim}")   # arrayName.ndim gives dimensions of the array

# 1D array
n1 = np.array([2,3,5,6,1])
print(n1)
print(f"Dimensions are {n1.ndim}") 

# 2D array : combination of 2 1D arrays
n2 = np.array(
                [
                    [2,3,5,6,1],[3,4,51,6,9]
                ]
            )
print(n2)
print(f"Dimensions are {n2.ndim}") 

# 3D array : combination of 2 2D arrays
n3 = np.array(
                [
                    [
                        [1,2,3],[4,5,6],[7,8,9]
                    ],    # first layer
                    
                    [
                    [10,11,12],[13,14,15],[16,17,18]
                    ]# second layer
                ]
            )   
print(f"\n{n3}\nDimensions are {n3.ndim}")


# to create a 5D array from a 1D array

n4 = np.array([1,2,3,4,5],ndmin=5)
print(n4)
print(n4.ndim)

n5 = np.linspace(1,10,4)
print(n5)



