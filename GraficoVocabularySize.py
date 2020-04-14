from newsgroups import perceptron_20newsgroups
from reuters import perceptron_reuters
import matplotlib.pyplot as plt

X=[10,100,1000,2500,5000,10000,50000,100000]
count=0
Y1=[]
Y2=[]
while(count<len(X)):
    Y1.append(perceptron_20newsgroups(X[count]))
    Y2.append(perceptron_reuters(X[count]))
    count=count+1
print(Y1)
print(Y2)

plt.plot(X, Y1, marker='o',color='magenta',label='20_newsgropus')
plt.plot(X,Y2, marker='s', color='blue',label='reuters-21578')
plt.title("20 newsgroups and Reuters-21578")
plt.xlabel("Vocabulary size")
plt.ylabel("Classification accuracy")
plt.xticks(ticks=[10,100,1000,2500,5000,10000,50000,100000])
plt.xscale('log')
plt.legend()
plt.show()
