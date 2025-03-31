# we need to predict per capital income of year 2020

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

trainingData = pd.read_csv(r'D:\CODING_CODES\AIML\Machine Learning\Linear Regression\canada_per_capita_income.csv')

model = linear_model.LinearRegression()
x = trainingData.drop('per capita income (US$)',axis='columns')
y = trainingData['per capita income (US$)']
model.fit(x,y)

print(model.predict(pd.DataFrame({'year':[2020]})))