import pandas as pd
# viewing the data quickly: head() method
# returns headers and number of specified rows

# printing first 10 rows of dataset.json file
df = pd.read_json(r"D:\CODING_CODES\AIML\Pandas\dataset.json")
print(df.to_string())
print("\nUsing head method:")
print(df.head(10))
# without argumens i.e df.head() returns first 5 rows
print(df.head())
# df.tail(n) returns last n rows
print(df.tail(10))
# without argumens i.e df.tail() returns last 5 rows
print(df.tail())

# printing info about df -> df.info()
print(df.info())