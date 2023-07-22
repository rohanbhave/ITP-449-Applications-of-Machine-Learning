# Rohan Bhave
# ITP 449
# HW4
# Q1

# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# generating series of random numbers
# upper limit not inclusive
X = pd.Series(np.random.randint(low = 1,high = 201, size = 200))
Y = pd.Series(np.random.randint(low = 1,high = 200, size = 200))

# plotting x against y 
plt.scatter(X,Y, color = "r", s = 10)

# setting plot visual features
plt.title("Scatter of random integers", color = "g")
plt.ylabel("Random integer", color = "b")
plt.xlabel("Random integer", color = "b")


plt.show()


