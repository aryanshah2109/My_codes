import pandas as pd
marks = [71,22,64,63,49]
subjects = ['Maths','English','Science','Hindi','Gujarati']
marks_data = pd.Series(marks,index=subjects,name="Aryan's Data")
print(marks_data)

# size : number of rows in series
print(marks_data.size)

# dtype
print(marks_data.dtype)

# name
print(marks_data.name)

# is_unique : return true if all values are unique else false
print(marks_data.is_unique)

print(marks_data.index)

print(marks_data.values)    
