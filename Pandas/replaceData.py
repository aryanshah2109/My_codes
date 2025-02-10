import pandas as pd
import numpy as np
data = {"ID":[1,2,3,4,5],
        "Name":["Aryan","Jay","Rahil","Prem","Krish"],
        "Salary":[100066,None,4515,3611,26161]}
df = pd.DataFrame(data)
print(df)

# overwriting existing data
print("\nUpdated Value\n")
df.loc[1,"Salary"] = 1
print(df)

# for larger data sets we can use loops 
# suppose we need to replace salary to 10000 if salary > 10000
print("\nUpdated Value With loops\n")
for i in df.index:
    if df.loc[i,"Salary"] > 10000:
        df.loc[i,"Salary"] = 10000
print(df)

# we can also remove that row
df2 = pd.DataFrame(data)
print("\nUpdated Value With Removal\n")
for i in df.index:
    if df.loc[i,"Salary"] > 5000:
        df.drop(i,inplace=True)
print(df)