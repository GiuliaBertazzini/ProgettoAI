from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import numpy as np

def perceptron_20newsgroups(vocabulary_size=10000, cats=4):
    categories =[]
    count=0
    while(count<cats):
        categories.append(fetch_20newsgroups(subset='train').target_names[count])
        count=count+1

    newsgroups_train = fetch_20newsgroups(subset='train', categories=categories,
                                          remove=('headers', 'footers', 'quotes'))
    newsgroups_test = fetch_20newsgroups(subset='test',  categories=categories, remove=('headers', 'footers', 'quotes'))

    vectorizer = CountVectorizer(max_features=vocabulary_size)
    X_train = vectorizer.fit_transform(newsgroups_train.data)
    X_test = vectorizer.transform(newsgroups_test.data)

    classifier = Perceptron(max_iter=100, eta0=0.01)
    classifier.fit(X_train, newsgroups_train.target)
    predictions = classifier.predict(X_test)

    return accuracy_score(newsgroups_test.target, predictions)
