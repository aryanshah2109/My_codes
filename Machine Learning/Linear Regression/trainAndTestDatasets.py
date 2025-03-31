from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\CODING_CODES\AIML\Linear Regression\carpricesTrainTest.csv')

from sklearn.model_selection import train_test_split
X = df[['Mileage','Age(yrs)']]
y = df['Sell Price($)']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
print("Testing feature data \n",X_test)
print("Training feature data \n",X_train)
print("Testing target data \n",y_test)
print("Training target data \n",y_train)

# linear regression model
model = linear_model.LinearRegression()
model.fit(X_train,y_train)
print(model.predict(X_test))
print(model.score(X_test,y_test))