#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap


#df = pd.read_csv("C:\\Users\\brian\\Documents\\Python\\Python Data\\BeerDataset.csv")
df = pd.read_excel('C:\\Users\\brian\\Documents\\Python\\Python Data\\BeerDataset.xlsx', index_col=0)  
df.head()


df.shape


X = df.iloc[:,0:13]


#X = df[['Malic_Acid','Ash','Ash_Alcanity','Magnesium','Total_Phenois','Flavanoids','Nonflavanoid_Phenois','ProanThocyanins','Color_Intensity','Hue','OD280','Proline']].values


y = df["Beer_Grade"]
#y = df.iloc[:13]
#y[0:13]


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25,random_state = 0)


from sklearn.svm import SVC
clf = SVC(kernel='rbf',random_state=0)
clf.fit(X_train,y_train)


y_pred = clf.predict(X_test)


from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=clf,X=X_train,y=y_train,cv=10)


accuracies.mean()
accuracies.std()
print(accuracies.mean())
print(accuracies.std())

X_set, y_set = X_train, y_train
#X_set[:,0]
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
np.arange(start = y_set[:, 1].min() - 1, stop = y_set[:, 1].max() + 1, step = 0.01))

plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green', 'blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green', 'blue'))(i), label = j)
plt.title('Kernel SVM (Training set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()




