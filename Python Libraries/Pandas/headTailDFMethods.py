import pandas as pd
# viewing the data quickly: head() method
# returns headers and number of specified rows

# printing first 10 rows of dataset.json file
df = pd.read_json(r"D:\CODING_CODES\AIML\Python Libraries\Pandas\Files\dataset.json")
print(df.to_string())
print("\nUsing head method:")
print(df.head(10))
# without argumens i.e df.head() returns first 5 rows
print("\nUsing head method without arguments:")
print(df.head())
# df.tail(n) returns last n rows
print("\nUsing tail method:")
print(df.tail(10))
# without argumens i.e df.tail() returns last 5 rows
print(df.tail())
print("\nUsing tail method without arguments:")
# printing info about df -> df.info()
print(df.info())

print("\nUsing sample method to get a random value:")
print(df.sample())

print("\nUsing sample method with argument to get a random value:")
print(df.sample(5)) # returns 5 random rows

# value_counts returns frequency of each value in dataframe in descending order
print("\nUsing value_counts:")
print(df.value_counts())




# printing all other featuers of a dataframe -> df.describe() 
print("\nUsing describe method to get details of dataframe:")
print(df.describe())


df = pd.read_csv(r"D:\CODING_CODES\AIML\Python Libraries\Pandas\Files\MyData.csv")
# sort_values sorts inplace, for descending order set argument
# ascending = False
print("\nUsing sort_values: ")
print(df.sort_values(by="Age").to_string()) # doesnt does inplace
# to make inplace set  sort_values(by="Age",inplace=True)

print(df.sort_values(by="Age",ascending=False).to_string())

print("\nUsing count method")
# count returns number of items 
# diff bw count and size is count doesnt consider NaN values
# but size does
print(df.count())
