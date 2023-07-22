# Rohan Bhave
# ITP 449
# Project
# Q3

# loading dataset
import pandas as pd

myDF = pd.read_csv("UniversalBank.csv")
print(myDF)

# A. target = "Personal Loan"
y = myDF["Personal Loan"]

# C. Partitioning data 75/25
X = myDF.drop(["Row", "ZIP Code", "Personal Loan"], axis=1, inplace=False)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=2023, stratify=y)

# D. how many cases in training partition represent people who accepted offer
accepted = y_train.sum()
print("Training set acceptances:", accepted)

# E. plot classification tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion="entropy", max_depth=5, random_state = 2023)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plot_tree(model, fontsize=8, feature_names=X.columns)
plt.show()

# generating confusion matrix
from sklearn import metrics
# metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
# plt.show()

# F. acceptors classified as non-acceptors
print("acceptors classifed as non-acceptors:", metrics.confusion_matrix(y_test, y_pred)[1, 0])

# G. non-acceptors classifed as acceptors
print("non-acceptors classifed as acceptors:", metrics.confusion_matrix(y_test, y_pred)[0, 1])

# H. accuracy on training partition
print("train accuracy:", model.score(X_train, y_train))
# I. accuracy on tests partition
print("test accuracy:", model.score(X_test, y_test))


