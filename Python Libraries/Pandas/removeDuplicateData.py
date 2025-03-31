import pandas as pd
data = {"ID":[1,2,2,4,5],
        "Name":["Aryan","Rahil","Rahil","Prem","Krish"],
        "Salary":[100066,4515,4515,3611,26161]}
df = pd.DataFrame(data,index=None)
print(df)
print(df.duplicated())      # returns True if there is any duplications

df.drop_duplicates(inplace=True)    # inplace changes in original df
                                    # it doesnt create a copy
print(df)