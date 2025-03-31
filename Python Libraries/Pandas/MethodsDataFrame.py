import pandas as pd

data = {"ID":[1,2,3,4,5],
        "Name":["Aryan","Jay","Rahil","Prem","Krish"],
        "Salary":[100066,None,45151,13611,26161],
        "Age":[10,20,30,40,50]}

df = pd.DataFrame(data)

# filtering single condition
df = df[df["ID"]>2]
print(df)

# filtering multiple conditons
df = pd.DataFrame(data)
df = df[(df["ID"]>2) & (df["Age"]>10)]

# sorting 
print("Sorted Values")
df = pd.DataFrame(data)
print(df.sort_values(by="Age",ascending=False))

# modifying columns
df["Age"] = df["Age"]*2
print(df)
