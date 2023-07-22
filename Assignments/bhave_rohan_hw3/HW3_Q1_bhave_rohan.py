# Rohan Bhave
# ITP 449
# HW3
# Question 1

# importing necessary libraries
import pandas as pd
import numpy as np

# 1. creating dictionary
myDict = {"attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
          "name"    : ["Anastasia", "Dima", "Katherine", "James", "Emily", "Michael", "Matthew", "Laura", "Kevin", "Jonas"],
          "qualify" : ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"],
          "score"   : [12.5, 9.0, 16.5, np.nan, 9.0, 20.0, 14.5, np.nan, 8.0, 19.0]}

# creating dataframe from dictionary
myDF = pd.DataFrame(myDict)

# 2. printing name and attempts
print(myDF[["name", "attempts"]])
print()

# 3. printing name and score of single-attempt, qualifying contestants
print(myDF[["name", "score"]][np.logical_and(myDF["attempts"] == 1, myDF["qualify"] == "yes")])
print()

# 4. replacing NaN values with zero's
myDF.loc[np.isnan(myDF["score"]), "score"] = 0
print(myDF)
print()

# 5. print dataframe sorted by attempts
print(myDF.sort_values(by = ["attempts", "score"], ascending = [True, False], inplace = False))


