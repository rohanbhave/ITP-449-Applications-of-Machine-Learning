# Rohan Bhave
# ITP 449
# HW4
# Q2

# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading CSV
climateDF = pd.read_csv("climate.csv")
print(climateDF)

plt.title("Global temperature")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly")

# creating points
plt.scatter(climateDF["Year"], climateDF["Value"], color = "r")

# creating lines
plt.plot(climateDF["Year"], climateDF["Value"], color = "r", linestyle = "dashed")
# showing scatter plot
plt.show()