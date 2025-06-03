import pandas as pd
#cleaning data: fixing bad data in your file
# bad data can be empty values, incorrect format, incorrect data

# empty cell -> gives wrong results always
# so we have to remove rows with bad data

# here we will create a new dataframe with no empty cell

data = pd.read_csv(r"D:\CODING_CODES\AIML\Python Libraries\Pandas\Files\dirty_data_100.csv")
print(data.to_string())


# *** never modify original data file ***

print("\nCleaned data: ")
dataCleaned = data.dropna()
print(dataCleaned.to_string())
print("Before cleaning: ")
print(data.info())
print("After cleaning: ")
print(dataCleaned.info())
dataCleaned.to_csv(r"D:\CODING_CODES\AIML\Python Librarie\Pandas\Files\cleaned_Data.csv")

# to make changes to original file:
# data.dropna(inplace=True)

# to replace data, use fillna(new_value)
dataReplaced = data.fillna("Not known")
print(dataReplaced.to_string())
dataReplaced.to_csv(r"D:\CODING_CODES\AIML\Python Librarie\Pandas\Files\ReplacedData.csv")
# to replace in original file, data.fillna(replaced_data,inplace=True)

# to replace only particular column empty value, you need to specify
# column name
data["ID"] = data["ID"].fillna("ID --")
print(data.to_string())
data.to_csv(r"D:\CODING_CODES\AIML\Python Librarie\Pandas\Files\ParticularReplacedData.csv")
