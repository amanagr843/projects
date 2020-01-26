import numpy as np
import  matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('sal.csv',
                    names=['age',
                           'workclass',
                           'fnlwgt',
                           'education',
                           'education-num',
                           'marital-status',
                           'occupation',
                           'relationship',
                           'race',
                           'gender',
                           'capital-gain',
                           'capital-loss',
                           'hours-per-week',
                           'native-country',
                           'salary'
                           ], na_values=' ?')

X=dataset.iloc[:,0:14].values
y=dataset.iloc[:,-1].values

from sklearn.impute import SimpleImputer
sim= SimpleImputer()
X[:,[0,2,4,10,11,12]]=sim.fit_transform(X[:,[0,2,4,10,11,12]])

test=pd.DataFrame(X[:,[1,3,5,6,7,8,9,13]])
test[0].value_counts()
test[1].value_counts()
test[2].value_counts()
test[3].value_counts()
test[4].value_counts()
test[5].value_counts()
test[6].value_counts()
test[7].value_counts()

test[0]=test[0].fillna(' Private')
test[1]=test[1].fillna(' HS-grade')
test[2]=test[2].fillna(' Married-civ-spouse')
test[3]=test[3].fillna(' Prof-specialty')
test[4]=test[4].fillna(' Husband')
test[5]=test[5].fillna(' White')
test[6]=test[6].fillna(' Male')
test[7]=test[7].fillna('  United-States')
X[:,[1,3,5,6,7,8,9,13]]=test

from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
X[:,1]=lab.fit_transform(X[:,1])
X[:,3]=lab.fit_transform(X[:,3])
X[:,5]=lab.fit_transform(X[:,5])
X[:,6]=lab.fit_transform(X[:,6])
X[:,7]=lab.fit_transform(X[:,7])
X[:,8]=lab.fit_transform(X[:,8])
X[:,9]=lab.fit_transform(X[:,9])
X[:,13]=lab.fit_transform(X[:,13])
lab.classes_

from sklearn.preprocessing import OneHotEncoder
one= OneHotEncoder(categorical_features=[1,3,5,6,7,8,9,13])
X=one.fit_transform(X)
X=X.toarray()

y=lab.fit_transform(y)
lab.classes_
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(X)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)

from sklearn.tree import DecisionTreeClassifier
dtf=DecisionTreeClassifier()
dtf.fit(X_train,y_train)

dtf.score(X_train,y_train)
dtf.score(X_test,y_test)
dtf.score(X,y)

from sklearn.tree import export_graphviz
export_graphviz(dtf,out_file="tree4.dot")

import pydotplus
dot_data = StringIO()



from graphviz import Source
file=open("tree4.dot","r")
text=file.read()
Source(text)