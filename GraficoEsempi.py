from newsgroups import perceptron_20newsgroups
from reuters import perceptron_reuters
import matplotlib.pyplot as plt
import numpy as np

x=[2,3,4,5,6,7,8,9,10]
count=0
y1=[]
y2=[]
while(count<len(x)):
    y1.append(perceptron_20newsgroups(cats=x[count]))
    y2.append(perceptron_reuters(cats=x[count]))
    count=count+1

X=[100,500,1000,2000,3000,4000,5000,6000,7000]
ynumbers=np.linspace(start=0,stop=1,num=10)

plt.plot(X,y1, marker='o',color='magenta',label='20_newsgropus')
plt.plot(X,y2, marker='s', color='blue',label='reuters-21578')
plt.title("20 newsgroups and Reuters-21578")
plt.xlabel("Samples")
plt.ylabel("Classification accuracy")
plt.yticks(ynumbers)
plt.legend()
plt.show()
