import pandas as pd
from sklearn.tree import  DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names = ["pregnant","glucose","bp","skin","insulin","bmi","pedigree","age","label"]

pima = pd.read_csv('diabetes.csv',header=None,names=col_names)

print(pima.head(10))

feature_cols = ["pregnant","insulin","bmi","age","glucose","bp","pedigree"]
X = pima[feature_cols]
y = pima.label

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=42)

clf = DecisionTreeClassifier(max_depth=22)
clf = clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

print(f"dokładnośc dopaswania wyników: {metrics.accuracy_score(y_test,y_pred)}")
