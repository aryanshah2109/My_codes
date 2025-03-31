import numpy as np
arr = np.array([1,2,3,4,5,6])

# np.exp(arr) returns array of exponential values of the array elements
print(np.exp(arr))

# np.log(arr) returns array of logarithmic values of the array elements base e
print(np.log(arr))

# np.log10(arr) returns array of logarithmic values of the array elements base 10
print(np.log10(arr))

print(np.sum(arr))  # returns sum of elements of array

arr = np.random.randint(1,10,size=8)
print(arr)
print(np.argmax(arr))   # returns index of maximum element
print(np.argmin(arr))   # returns index of minimum element

arr = np.array([-1.74213, 2.434355, 9.253194, -1.52492, -5.352483])
print(arr)
print(np.abs(arr))      # converts all negatives to positives
print(np.round(arr,2))  # rounds up array elements upto given number of decimal points