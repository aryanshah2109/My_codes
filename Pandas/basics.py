import pandas as pd
print(pd.__version__)

# a pandas series is like a column in a table
# it is like a 1D array which stores data of any type
# here we will create a simple pandas series
aryan = [1,2,3]
aryanNew = pd.Series(aryan)
print(aryanNew) # output will give indexing and values and dtype

# labelling in a series i.e accessing elements of a series
print(aryanNew[0])

# with index=[newIndices] in Series functions, you can create your own labels(indices)
aryan = [1,2,3]
aryanNew = pd.Series(aryan,index=["x","y","z"])
print(aryanNew)
print(aryanNew["y"])

# accessing dictionary items
dict = {"day1" : 3, "day2" : 9, "day3" : 10, "day4" : 14}
result = pd.Series(dict, index=["day1","day4"])     # accessing dictionary items
print(result)   
