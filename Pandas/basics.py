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