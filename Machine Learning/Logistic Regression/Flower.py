import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

x=iris.data
y=iris.target
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
model.fit(x_train,y_train)
print(model.predict(x_test))
print(y_test)
print(model.score(x_test,y_test))

