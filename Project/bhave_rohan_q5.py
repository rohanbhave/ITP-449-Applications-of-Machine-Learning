'''
0 is the missing value not null
don't want to drop the 0s
replace 0s with means
myDF["insulin"] not zero mean. don't include 0 in mean
0 is valid for preganncies
create sample that contains those number 6, 140, but can't pass into model directly. Scale it first 
'''

# Rohan Bhave
# ITP 449
# Project
# Q5

import pandas as pd

# 1. create DataFrame, view all columns
diabetes_knn = pd.read_csv("diabetes.csv")
pd.set_option('display.max_columns', None)
print(diabetes_knn)

# 2. determine dimensions of DF
print("dimensions:", diabetes_knn.shape)

# 4. Create Feature Matrix and Target Vector
X = diabetes_knn.iloc[:, : -1]
y = diabetes_knn.iloc[:, -1]

# 3. replacing zeros
X.iloc[:, 1:] = X.iloc[:, 1:].replace(0, X.iloc[:, 1:][X.iloc[:, 1:] != 0].mean())

# 5. Standardize attributes of Feature Matrix
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)   # scaling features
XScaled = pd.DataFrame(data=scaler.transform(X), columns = X.columns)

# 6. Split features and target
from sklearn.model_selection import train_test_split
X_trainA, X_trainB, y_trainA, y_trainB = train_test_split(XScaled, y, test_size=0.30, random_state = 2023, stratify=y)

# 7. Develop KNN and obtain KNN score for A and B
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
neighbors_range = range(1, 9)
scoresA = []    # creating scores lists
scoresB = []
for n in neighbors_range:   # looping through # of neighbors
    model = KNeighborsClassifier(n_neighbors=n)
    model.fit(X_trainA, y_trainA)
    scoresA.append(model.score(X_trainA, y_trainA))
    scoresB.append(model.score(X_trainB, y_trainB))

# 8. Plot graph of A and B and deteremine best value of k
plt.plot(neighbors_range, scoresA, label = "Train A")   # plotting A and B scores
plt.plot(neighbors_range, scoresB, label = "Train B")
plt.xticks(neighbors_range)
plt.xlabel("Neighbors")
plt.ylabel("Score")
plt.legend()
plt.show()
# best k = 4

# 9. display score of model with best value of k
model = KNeighborsClassifier(n_neighbors=4)
model.fit(X_trainA, y_trainA)
y_predB = model.predict(X_trainB)
print("model score:", model.score(X_trainB, y_trainB))

# print and plot confusion matrix
from sklearn import metrics
print(metrics.confusion_matrix(y_trainB, y_predB))
metrics.ConfusionMatrixDisplay.from_predictions(y_trainB, y_predB)
plt.show()

# 10. predict outcome
sample = [[6, 140, 60, 12, 300, 24, 0.4, 45]]
sample_scaled = pd.DataFrame(data=scaler.transform(sample), columns = X.columns)
sample_predict = model.predict(sample_scaled)
print("sample prediction:", sample_predict)










