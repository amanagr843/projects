import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import nltk
nltk.download("stopwords")
import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
ps= SnowballStemmer("english")

dataset= pd.read_csv("data.csv")

dataset = dataset.drop(columns = "Unnamed: 0")

processed_reviews = []

for i in range(0,37):
    temp = re.sub("[^a-zA-Z]"," ",dataset["Reviews"][i])
    temp = temp.lower()
    temp = temp.split()
    temp =[ps.stem(token) for token in temp if not token in set(stopwords.words("english"))]
    temp=" ".join(temp)
    processed_reviews.append(temp)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(processed_reviews)
cv.get_feature_names()
X = X.toarray()
y = dataset["P/N"].values

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
y = lb.fit_transform(y)
selector = SelectKBest(chi2, k=150)
selector.fit(X, y)
top_words = selector.get_support().nonzero()
X1 = X[:,top_words[0]]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X1,y)


from sklearn.naive_bayes import GaussianNB
nb=GaussianNB()
nb.fit(X_train,y_train)

nb.score(X_test,y_test)
nb.score(X_train,y_train)
nb.score(X1,y)











    
    