# Rohan Bhave
# ITP 449
# HW6
# Q2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# reading csv
myDF = pd.read_csv("CommuteStLouis.csv")

# printing summary of DF
print(myDF.describe())

# plotting histogram
plt.hist(myDF["Age"])
plt.title("Histogram of Age")
plt.ylabel("Freq")
plt.xlabel("Age")

plt.show()

# correlation matrix
print(myDF.corr(numeric_only=True))
# distance and time most closely correlated (corr = 0.83)

# creating pairplot
import seaborn as sn
sn.pairplot(myDF)
plt.show()
# diagonal shows histogram of each value
# all values skewed left

# boxplot male and female
sn.boxplot(data = myDF, x = "Sex", y = "Distance")
plt.show()
# on average women commute shorter distances

# scatter plot between distance and time
plt.scatter(myDF["Distance"], myDF["Time"])
plt.ylabel("Time")
plt.xlabel("Distance")
plt.suptitle("Scatterplot and Linear Regression of Time vs Distance")

# creating linear regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()

X = myDF["Distance"].values.reshape(-1, 1) # turning series in array and reshaping
y = myDF["Time"]
model.fit(X, y)

xLine = np.linspace(0, 80, num=100).reshape(-1, 1)
yLine = model.predict(xLine)
plt.plot(xLine, yLine)
plt.show()

# showing distribution of residuals
from yellowbrick.regressor import ResidualsPlot
vis = ResidualsPlot(model)
vis.fit(X, y)
vis.show()








