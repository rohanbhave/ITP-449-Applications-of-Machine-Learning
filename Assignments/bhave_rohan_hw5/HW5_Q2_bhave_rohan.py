# Rohan Bhave
# ITP 449
# HW5
# Q2

# importing libraries
import pandas as pd


# reading csv file and printing
myDF = pd.read_csv("mtcars.csv")

# creating DF with  ‘Car Name’, ‘cyl’, ’gear’, ‘hp’, ‘mpg’
carDF = myDF.loc[:, ["Car Name", "cyl", "gear", "hp", "mpg"]]
carDF.set_index("Car Name") # setting index to Car Name
carDF.rename(columns={"cyl":"cylinder", "gear":"Gear", "hp":"Horsepower", "mpg":"Miles Per Gallon"}, inplace=True)
print(carDF)
print()

# new column stating if horsepower at least 110
carDF["Powerful"] = carDF["Horsepower"] >= 110
print(carDF)
print()

# printing without horsepower column
print(carDF.drop("Horsepower", axis=1, inplace=False))
print()

# printing cars with mpg greater than 25.0
print(carDF.loc[carDF["Miles Per Gallon"] > 25.0,:].sort_values(by = "Horsepower", ascending=False))
print()

# car that is powerful and has highest miles per gallon
print(carDF.loc[carDF["Powerful"]].sort_values(by="Miles Per Gallon", ascending=False).head(1))