# Rohan Bhave
# ITP 449
# Project
# Q4

import pandas as pd

# reading csv
myDF = pd.read_csv("mushrooms.csv")
print(myDF)

# assigning feature and target
X = myDF.iloc[:, 1:]
y = myDF.iloc[:, 0]

# getting dummies for X
X_dummies = pd.get_dummies(X, drop_first=True)

# splitting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_dummies, y, train_size=0.75, random_state=2023, stratify=y)

# making tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=6)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# A. making confusion matrix
from sklearn import metrics
import matplotlib.pyplot as plt
print(metrics.confusion_matrix(y_test, y_pred))
metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

# B. accuracy of training partition
from sklearn import metrics
print("training accuracy:", metrics.accuracy_score(y_train, model.predict(X_train)))

# C. accuracy of test partition
print("test accuracy:", metrics.accuracy_score(y_test, model.predict(X_test)))

# D. show classification tree
from sklearn.tree import plot_tree
plot_tree(model, fontsize=8, feature_names=X_dummies.columns, class_names=y.unique(), filled=True)
plt.show()

# E. list top three most important features
featuresDF = pd.DataFrame(model.feature_importances_, index=X_dummies.columns)
print(featuresDF.sort_values(by=0, ascending=False).head(3))

# F. classifying unknown mushroom
# making copy of features
X2 = X.copy()

# creating unknown sample
sample = pd.DataFrame([["x","s","n","t","y","f","c","n","k","e","e","s","s","w","w","p","w","o","p","r","s","u"]], columns=X2.columns)

# concatenating sample into X2
X2 = pd.concat([X2, sample])

# getting dummies for X2
X2_dummies = pd.get_dummies(X2, drop_first=True)
sample_dummy = X2_dummies.tail(1)   # dummy of unknown

# predicting
y_pred_sample = model.predict(sample_dummy)
print("uknown sample:", y_pred_sample)







