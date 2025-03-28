import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

trainingData = pd.read_csv(r'D:\CODING_CODES\AIML\Linear Regression\hiring.csv')

# cleaning data
trainingData.experience = trainingData.experience.fillna(trainingData.experience.median())
trainingData['test_score(out of 10)'] = trainingData['test_score(out of 10)'].fillna(trainingData['test_score(out of 10)'].median())

model = linear_model.LinearRegression()

x = trainingData.drop('salary($)',axis='columns')
y = trainingData['salary($)']

model.fit(x,y)

print(model.predict(pd.DataFrame([[2,9,6]],columns=x.columns)))



