# Rohan Bhave
# ITP 449
# Project
# Q1

import pandas as pd

# A. Load data
myDF = pd.read_csv("winequality.csv")
print(myDF)

# B. Standardize all variables other than Quality
X = myDF.iloc[:, : -1]
y = myDF.iloc[:, -1]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)   # scaling features
XScaled = pd.DataFrame(data=scaler.transform(X), columns = X.columns)

# C. Partition dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(XScaled, y, test_size = 0.2, random_state = 2023, stratify=y)
X_trainA, X_trainB, y_trainA, y_trainB = train_test_split(X_train, y_train, test_size = 0.25, random_state = 2023, stratify=y_train)

# D. Build KNN classification
# E. Iterate on K ranging from 1 to 30, plot accuracy and A and B
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

neighbors_range = range(1, 31)
scoresA = []    # creating scores lists
scoresB = []
for n in neighbors_range:   # looping through # of neighbors
    model = KNeighborsClassifier(n_neighbors=n)
    model.fit(X_trainA, y_trainA)
    scoresA.append(model.score(X_trainA, y_trainA))
    scoresB.append(model.score(X_trainB, y_trainB))


plt.plot(neighbors_range, scoresA, label = "Train A")   # plotting A and B scores
plt.plot(neighbors_range, scoresB, label = "Train B")
plt.xticks(neighbors_range)
plt.legend()
plt.show()

# F. Which value of k produced best accuracy
# k = 1 in A and k = 27 in B (27 is overall the best)

# G. Generate prediction for test partitions with chosen value of k
model = KNeighborsClassifier(n_neighbors=27)
model.fit(X_trainA, y_trainA)
y_pred = model.predict(X_test)

from sklearn import metrics
# printing accuracy
print("Train A Accuracy:",model.score(X_trainA, y_trainA))
print("Train B Accuracy:",model.score(X_trainB, y_trainB))
# plot confusion matrix
metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

# H. print test dataframe with added columns quality and predicted quality
testDF = X_test.copy()
testDF["Quality"] = y_test
testDF["Predicted Quality"] = y_pred
print(testDF)

# I. print accuracy of model on test dataset
print("Test Accuracy:",model.score(X_test, y_test))

