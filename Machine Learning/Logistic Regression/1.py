import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\CODING_CODES\AIML\Machine Learning\Logistic Regression\insurance_data.csv')
plt.scatter(df['age'],df['bought_insurance'],marker='+',color='red')
# plt.show()

from sklearn.model_selection import train_test_split
x = df[['age']]
y = df.bought_insurance
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)
print(model.predict(x_test))
print(y_test)
print(model.score(x_test,y_test))