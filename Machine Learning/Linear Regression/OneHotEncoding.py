# used to handle text based data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv(r'D:\CODING_CODES\AIML\Linear Regression\OneHotEncodingHousePrices.csv')

# print(df.to_string())


dummies = pd.get_dummies(df.town,dtype=int)
print(dummies)  

df_dummies = pd.concat([df,dummies],axis='columns')
print(df_dummies.to_string())

# drop one column of onehot encoding, price and town column
df_dummies = df_dummies.drop(['town','west windsor'],axis='columns')

print(df_dummies.to_string())

x = df_dummies.drop(['price'],axis='columns')
y = df_dummies.price

model = linear_model.LinearRegression()
model.fit(x,y)

# price of area = 3600 in west windsor
# for west windsor, monroe township = 0 and robinsville = 0
print(model.predict(pd.DataFrame({'area':[3600],'monroe township':[0],'robinsville':[0]})))

# price of area = 2800 in robinsville
# for robinsville, monroe township = 0 and robinsville = 1
print(model.predict(pd.DataFrame({'area':[2800],'monroe township':[0],'robinsville':[1]})))