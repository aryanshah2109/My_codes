import numpy as np

# generates random integer
n1 = np.random.randint(1,14,size=(5))
print(n1)

# random 2D array 
# size = (3,5) 
# 3 -> no of rows
# 5 -> no of cols
n2 = np.random.randint(1,100,size=(3,5))
print(n2)



# generates random float value
n3 = np.random.rand()
print(n3)

# random 1D float array
n4 = np.random.rand(3)  # 3-> no. of elements
print(n4)

# random 2D float array
# 3 -> no of rows
# 5 -> no of cols
n5 = np.random.rand(3,5)
print(n5)