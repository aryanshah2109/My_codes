import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

iris = load_iris()
X = iris.data
y = iris.target

target_names = iris.target_names

X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=32)

model = RandomForestClassifier(random_state=32)
model.fit(X_train,y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))

print("Model accuracy: ", accuracy*100)

with open("D:/CODING_CODES/AIML/Streamlit/Practice/Fourth/model.pkl", "wb") as f:
    pickle.dump(model, f)