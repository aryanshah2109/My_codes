import pandas as pd
data = pd.read_json(r"D:\CODING_CODES\AIML\Pandas\salary_data.json")
print(data.to_string())

# we will replace the empty values with mean of the given values
x = data["salary"].mean()

data["salary"] = data["salary"].fillna(x)
print(f"Updated data with mean:\n{data}")

# similar with median
# x = data["salary"].median()
# data["salary"] = data["salary"].fillna(x)

# for with mode, we need to add [0] to x
data = pd.read_json(r"D:\CODING_CODES\AIML\Pandas\salary_data.json")

x = data["salary"].mode()[0]
data["salary"] = data["salary"].fillna(x)
print(f"Updated data with mode:\n{data}")