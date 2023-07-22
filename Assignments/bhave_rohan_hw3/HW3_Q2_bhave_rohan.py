# Rohan Bhave
# ITP 449
# HW3
# Question 2

# importing libraries
import pandas as pd
import numpy as np

# 1. reading csv file
DF = pd.read_csv("Trojans_roster.csv")
print(DF)
print()

# 2. setting index to player number
DF.set_index("#", inplace = True)
print(DF)
print()

# 3. removing last school and major columns from dataframe
DF.drop(["LAST SCHOOL", "MAJOR"], axis = 1, inplace = True)
print(DF)
print()

# 4. printing names of all quarterbacks
print(DF.loc[DF["POS."] == "QB"], "NAME")
print()

# 5. printing name, position, height, and weight of tallest player in the team
print(DF.loc[DF["HT."] == DF["HT."].max(), ["NAME", "POS.", "HT.", "WT."]])
print()

# 6. printing number of local players
print(DF.loc[DF["HOMETOWN"] == "Los Angeles, CA", "HOMETOWN"].value_counts())
print()

# 7. Printing 3 heaviest players
print(DF.sort_values(by="WT.", ascending = False)[0:3])
print()

# 8. adding BMI values to players
DF["BMI"] = 703 * DF["WT."]/(DF["HT."])**2
print(DF)
print()

# 9. printing mean and median of players' height, weight, and BMI
print("Height mean:", (DF["HT."].mean()))
print("Height median:", (DF["HT."].median()))

print("Weight mean:", (DF["WT."].mean()))
print("Weight median:", (DF["WT."].median()))

print("BMI mean:", (DF["BMI"].mean()))
print("BMI median:", (DF["BMI"].median()))
print()

# 10. printing mean and mean of players' height, weight, and BMI by position
print(DF.groupby("POS.")[["HT.", "WT.", "BMI"]].mean())
print()
print(DF.groupby("POS.")[["HT.", "WT.", "BMI"]].median())
print()

# 11. number of player in each position
print(DF.groupby("POS.")["POS."].count())
print()

# 12. printing players whose BMI is below team average
print(DF.loc[DF["BMI"] < DF["BMI"].mean(), "NAME"])
print()

# 13. Unique players' numbers
print(DF.index.unique())

