import pandas as pd

# dataframes: data sets in pandas are usually multidimensional tables and they are called dataframes
# series -> columns , dataframes -> whole tables

# creating a dataframe
dict2 = {"cal": [10,11,12], "dict2" : [93,24,19]}
result = pd.DataFrame(dict2, index=["a","b","c"])
print(result)

# locating / accessing a particular row of a dataframe
print(result.loc["a"])      # .loc[index] required

print(result.loc["c"])

# to access more than one rows, we add the row
# index in a list an then pass it in result.loc[list]

print(result.loc[["a","b"]])

# accessing particular column
print(result["cal"])

