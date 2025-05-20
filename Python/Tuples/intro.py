# tuple is immutable but list is mutable
tup = (1,4,9.5,"Aryan",True)
print(tup)
print(type(tup))
# tup[3] = 1
# print(tup)    immutable hence gives error
print("\nPrinting the tuple elements:")
for i in range(len(tup)):
    print(tup[i])

print(len(tup))

# tuple slicing
# tuple slicing creates a new tuple from the existing tuple
# i.e. tup2 is created while tup is sliced
# tup2 = tup[start : end : jump_index]
 
print(tup[:])           # prints entire tuple
print(tup[1:])          # prints entire tuple starting from index 1
print(tup[1:4])         # prints entire tuple from index 1,2,3
print(tup[1:4:2])       
# prints entire tuple and jumps twice between each index so prints index 1,3

# used if we want to check whether item is in the tuple
# kinda like linear search but we cannot find position 
if "Aryan" in tup:    
    print("Aryan is present in tuple")
else:   
    print("Aryan is not in tuple")


# when we create a tuple of just one element, i.e. tup = (1)
# python interpreter will think that tup is a variable instead of a tuple
# to avoid this, add a comma after the element i.e. tup = (1,)