# Rohan Bhave
# ITP 449
# HW5
# Q1

# importing libraries
import pandas as pd


# reading csv file and printing
myDF = pd.read_csv("mtcars.csv")
print(myDF)
print()

# setting Car Name as index
myDF.set_index("Car Name", inplace = True)
print(myDF)


