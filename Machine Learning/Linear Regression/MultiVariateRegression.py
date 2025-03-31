
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

trainingData = pd.read_csv(r'D:\CODING_CODES\AIML\Linear Regression\MVLR1.csv')

# cleaning data
trainingData.bedrooms = trainingData.bedrooms.fillna(trainingData.bedrooms.median())

model = linear_model.LinearRegression()
x = trainingData.drop(['price','Unnamed: 0'],axis='columns')
y=trainingData.price
model.fit(x,y)


print(model.predict(pd.DataFrame([[3000,3,10]],columns=x.columns)))
