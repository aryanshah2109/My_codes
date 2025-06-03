# csv file -> comma seperated file
# can contain huge amounts of data sets
# contains plain text
# when sending path in read_csv(), use raw string
# read_csv(r"path")

import pandas as pd
df = pd.read_csv(r"D:\CODING_CODES\AIML\Python Libraries\Pandas\Files\data.csv")
print(df.to_string())

# we can also directly print df but in this case if
# data is too large, then some of the data might 
# get skipped. Hence we print df.to_string()

# to check how many rows our system can print without
# using to_string(), we can 
# print(pd.options.display.max_rows)

print(pd.options.display.max_rows)
# if rows in csv file > max_rows, and 
# we have not used .to_string() then we will not see all the rows


df = pd.read_csv(r"D:\CODING_CODES\AIML\Pandas\Files\random_data_200.csv")
print(df)
print(df.to_string())

# we can increase max rows limit by pd.options.display.max_rows = new_limit
# but this can lead to hardware damage
# after increasing limit, we can then entire dataset byprint df 
# till the new limit
