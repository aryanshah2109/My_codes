# we have a csv file of multiple house areas and want to predict
# prices for each

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv(r'D:\CODING_CODES\AIML\Linear Regression\Predict.csv')
training_set = pd.read_csv(r'D:\CODING_CODES\AIML\Linear Regression\One.csv')
model = linear_model.LinearRegression()
new_df = training_set.drop('Price',axis='columns')
model.fit(new_df,training_set.Price)

predictedValues = model.predict(df)
print(predictedValues)

import pickle
with open(r'D:\CODING_CODES\AIML\Linear Regression\house_price_model_pickle','wb') as f:
    pickle.dump(model,f)

with open(r'D:\CODING_CODES\AIML\Linear Regression\house_price_model_pickle','rb') as file:
    mp = pickle.load(file)

print(mp.coef_)