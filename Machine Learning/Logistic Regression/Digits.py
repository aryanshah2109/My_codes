import pandas as pd
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()
# print(digits.images[0])
# for i in range(5):
#     plt.matshow(digits.images[i])
#     plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
x = digits.data
y = digits.target

model = LogisticRegression()
x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.2)
model.fit(x_train,y_train)
print(model.predict(x_test))
print(y_test)
print(model.score(x_test,y_test))

# we can find out which output was right and wrong by
# confusion matrix
from sklearn.metrics import confusion_matrix
y_pred = model.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print(cm)