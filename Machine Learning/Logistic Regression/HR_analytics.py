import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'D:\CODING_CODES\AIML\Machine Learning\Logistic Regression\HR_comma_sep.csv')

x = df.drop(['left','Department','salary'],axis='columns')
y = df.left

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

model = LogisticRegression()
model.fit(x_train,y_train)
print(model.predict(x_test))
print(y_test)
print(model.score(x_test,y_test))