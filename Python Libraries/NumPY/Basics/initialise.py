'''
1) np.zeroes((rows,cols))
2) np.full((rows,cols),number)
3) np.arange(lower,upper,jump)  -> lower to upper-1 with a jump of jump
4) np.random.randint(lower,upper,numberOfIntegersRequired)
'''




# we can initialise an array with zeroes by np.zero((rows,columns))
import numpy as np

n = np.zeros((2,4)) 
print(n)

n2 = np.zeros([5,5])
print(n2)

# we can initialise an array with the same number as np.full((rows,cols),number)
# first parameter is the dimension of the desired array and second parameter is the 
# number with which we want to initialise it
n3 = np.full((4,4),40)
print(f"\n{n3}\n")

# we can initialise an array within a particular range by np.arange(lower,upper,jump)
# it will initialise from lower to upper-1
n4 = np.arange(10,40)
print(f"\n{n4}\n")

n5 = np.arange(10,50,5)
print(f"\n{n5}\n")



# we can get random numbers in an array by
# np.random.randint(lower,upper-1,numberOfIntegersRequired)

n6 = np.random.randint(1,100,10)
print(f"\n{n6}\n")

n7 = np.random.random((2,6))    # creates an array of given rows and cols of random
                                # floats b/w 0 and 1
print(n7)