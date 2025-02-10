import pandas as pd
import numpy as np
data = {"ID":[1,2,3,4,5],
        "Name":["Aryan","Jay","Rahil","Prem","Krish"],
        "Salary":[100066,None,45151,13611,26161]}
df = pd.DataFrame(data)
print(df)

print("\nUpdated Value\n")
df["Salary"] = df["Salary"].replace({np.nan:"x000"})
print(df)