import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# 3 steps:
# 1) Make object of model by linear_model.LinearRegression()
# 2) Train it by model.fit(dataframe1,dataframe2)
# 3) Predict by model.predict(dataframeOfPrediction)


dict = {'Area':[2600,3000,3200,3600,4000],
        'Price':[550000, 565000, 610000, 680000, 725000]}
df = pd.DataFrame(dict)
plt.xlabel('Area')
plt.ylabel('Price in $')
plt.scatter(df.Area, df.Price, color='red',marker='+')
# plt.show()

new_df = df.drop('Price',axis='columns')

model = linear_model.LinearRegression()
model.fit(new_df,df.Price)

prediction = pd.DataFrame({'Area':[3300]})
print(model.predict(prediction))

prediction2 = pd.DataFrame({'Area':[5000]})
print(model.predict(prediction2))

# we can find slope and y-intercept by model.coef_ and model.intercept_
print(model.coef_)
print(model.intercept_)