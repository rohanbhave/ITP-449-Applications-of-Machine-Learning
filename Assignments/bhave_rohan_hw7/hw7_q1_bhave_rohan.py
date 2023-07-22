# Rohan Bhave
# ITP 449
# HW7
# Q1

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

# loading csv file
myDF = pd.read_csv("auto-mpg.csv")
print(myDF)


print(myDF.describe())
# A. DF shows the stats for cars. mpg is miles per gallon

# mean and median of mpg
print("mpg mean:", myDF["mpg"].mean())
print("mpg median:", myDF["mpg"].median())
# C. mean is higher than median mpg --> high outliers in data --> right skewed

# making histogram of mpg
plt.hist(myDF["mpg"])
plt.xlabel("mpg")
plt.ylabel("Count")
plt.show()

# making pairplot
sn.pairplot(data=myDF.drop("No", axis=1))
plt.show()
print(myDF.corr(numeric_only=True))
# F. model year and acceleration appear to be the least correlated

# scatter plot of mpg and displacement
plt.scatter(myDF["displacement"], myDF["mpg"])
plt.xlabel("Displacement")
plt.ylabel("mpg")
plt.title("Displacement vs. mpg")
plt.show()

# creating linear regression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
X = myDF["displacement"].values.reshape(-1, 1) # turning series in array and reshaping
y = myDF["mpg"]
model.fit(X, y)

# value of intercept
print()
print("Intercept:", model.intercept_)
# value of coefficient
print("Coefficient:", model.coef_)
# equation
print("y =", model.coef_, "x +", model.intercept_)
# d. predicted value for mpg decreases as displacement increases

# e. car with displacement value of 200
print("200 displacement:", model.predict([[200]]))

# scatterplot superimposed over linear regression line
plt.scatter(myDF["displacement"], myDF["mpg"])

# creating regression line
yLine = model.predict(X)
plt.plot(X, yLine, "r-")

plt.xlabel("Displacement")
plt.ylabel("mpg")
plt.title("Displacement vs. mpg Linear Regression")
plt.show()

# plotting
plt.show()

# plotting residuals
# showing distribution of residuals
from yellowbrick.regressor import ResidualsPlot
vis = ResidualsPlot(model)
vis.fit(X, y)
vis.show()












