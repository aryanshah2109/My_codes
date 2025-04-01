import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'D:\CODING_CODES\AIML\Machine Learning\Decision Tree\titanic.csv',index_col=None)

index = df[['Pclass','Sex','Age','Fare']]
target = df['Survived']



sex_n = LabelEncoder()
index['Sex_n'] = sex_n.fit_transform(index['Sex'])
print(index.to_string(index=False))
index_n = index.drop(['Sex'],axis='columns')
print(index_n)
model = DecisionTreeClassifier()
model.fit(index_n,target)
print(model.predict([[2,55,16,0]]))

x_train, x_test, y_train, y_test = train_test_split(index_n,target,test_size=0.2)
