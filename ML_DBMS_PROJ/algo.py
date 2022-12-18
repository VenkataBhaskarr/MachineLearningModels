import numpy as np
import matplotlib.pyplot as plt
import sklearn as sklearn
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
data = pd.read_csv("/Applications/XAMPP/xamppfiles/htdocs/PHP/ml.csv")
dataclass = data["professorName"]
data = data.drop("professorName",axis=1)
X = data.iloc[:, 1:7]
X = X.values
a = np.array([8,7,8,9,10,10])
distances1 = np.linalg.norm(X - a, axis=1)
k = 3
nearest_neighbor_ids1 = distances1.argsort()[:k]
nearest_guess1 = dataclass[nearest_neighbor_ids1]
li = list(nearest_guess1)
max(set(li), key = li.count)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_iris
 
 
# Create feature and target arrays
y = dataclass
 
# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(
             X, y, test_size = 0.2, random_state=4)
 
knn = KNeighborsClassifier(n_neighbors=3)
 
alg = knn.fit(X_train, y_train)

pickle.dump(alg,open('iri.pkl','wb'))

