from newsgroups import perceptron_20newsgroups
from reuters import perceptron_reuters

accuracy_20newsgroups = perceptron_20newsgroups()
print("20 newsgroups accuracy: ")
print(accuracy_20newsgroups)

accuracy_reuters= perceptron_reuters()
print("Reuters accuracy: ")
print(accuracy_reuters)
