from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

def perceptron_reuters(vocabulary_size=10000, cats=10):
    reuters=load_files(container_path="/home/giulia/PycharmProjects/ProgettoAI/venv/data-set/training-set")
    categories = []
    count = 0
    while (count < cats):
        categories.append(reuters.target_names[count])
        count = count + 1

    reuters_train = load_files(container_path="/home/giulia/PycharmProjects/ProgettoAI/venv/data-set/training-set",categories=categories)
    reuters_test = load_files(container_path="/home/giulia/PycharmProjects/ProgettoAI/venv/data-set/test-set",categories=categories)

    vectorizer = CountVectorizer(max_features=vocabulary_size, stop_words='english')
    X_train = vectorizer.fit_transform(reuters_train.data)
    X_test = vectorizer.transform(reuters_test.data)

    classifier = Perceptron(max_iter=1000, eta0=0.01)
    classifier.fit(X_train, reuters_train.target)
    predictions = classifier.predict(X_test)

    return accuracy_score(reuters_test.target, predictions)
