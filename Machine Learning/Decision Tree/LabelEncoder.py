import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\CODING_CODES\AIML\Machine Learning\Decision Tree\salaries.csv')

inputs = df.drop('salary_more_than_100k',axis='columns')
target=  df['salary_more_than_100k']
from sklearn.preprocessing import LabelEncoder
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_company.fit_transform(inputs['job'])
inputs['degree_n'] = le_company.fit_transform(inputs['degree'])


inputs_n = inputs.drop(['company','job','degree'],axis='columns')
print(inputs_n.to_string())

from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(inputs_n,target)
print(model.predict([[2,1,1]]))

# first = company (google- 2, facebook = 0, abc pharma=1)
# second = job (sales executive- 2, business manager = 0, company programmer=1)
# third = degree (bachelors- 0, masters = 1)