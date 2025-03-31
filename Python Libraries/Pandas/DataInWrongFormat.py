import pandas as pd
# to fix wrong format there are 2 ways:
# 1) remove the row
# 2) convert the format in the same format

data = {
    "ID" : [101,102,103,104,105],
    "Name" : ["Aryan","Rahil","Jay","Krish","Vansh"],
    "Age" : [19,25,13,49,15],
    "Salary" : [10000,404040,20403.99,49492,49245],
    "Join Date" : ["24/12/2020","21/02/2019","10/04/2011","14042011","19/04/2014"]
}
df = pd.DataFrame(data)
df.to_csv(r"D:\CODING_CODES\AIML\Pandas\Files\MyData.csv")

# errors = 'coerce' will ignore any errors if faced in formatting invalid dates

df["Join Date"] = pd.to_datetime(df["Join Date"], dayfirst=True, errors='coerce')
print(df.to_string())

