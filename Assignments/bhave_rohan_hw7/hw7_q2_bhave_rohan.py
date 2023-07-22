# Rohan Bhave
# ITP 449
# HW7
# Q2

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

myDF = pd.read_csv("Titanic.csv")
print(myDF)
# target variable is Survived

# dropping passenger #
myDF.drop(columns="Passenger", axis=1, inplace=True)
print(myDF)

# checking if null values
print(myDF.isnull().any(axis=0))
# no null values

# plotting countplots of remaining factors
sn.countplot(data=myDF, x="Class")
plt.show()
sn.countplot(data=myDF, x="Sex")
plt.show()
sn.countplot(data=myDF, x="Age")
plt.show()
sn.countplot(data=myDF, x="Survived")
plt.show()

# converting categorical variables into dummy variables
myDF2 = pd.get_dummies(data=myDF, columns = ["Class", "Sex", "Age"], drop_first=True)
print(myDF2)

# assigning X and y
X = myDF2.iloc[:, 1:]
y = myDF2["Survived"]

# partitioning data into train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size = 0.75, random_state=2023)

# fitting training data to logistic regression model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# displaying accuracy, precision, and recall
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

# displaying confusion matrix
from sklearn import metrics
# comparing y_test to y_pred

# plotting comparison
metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

# predicted value of survivability of adult, female, passenger 2nd class
passenger_sample = [[1, 0, 0, 0, 0]]
print("Predicted survivability:", model.predict(passenger_sample))
'''
# making dummies for age

# mapping dummy back to categorical value

class_2nd, class_3rd, class_Crew, sex_Female, Age_Adult
passenger_sample = [[1, 0, 0, 1, 1]]

model.predict(Passenger_sample)
'''


