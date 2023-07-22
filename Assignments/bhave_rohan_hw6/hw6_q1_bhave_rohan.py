# Rohan Bhave
# ITP 449
# HW6
# Q1

import pandas as pd
import matplotlib.pyplot as plt

# reading csv
avocado = pd.read_csv("avocado.csv")

# creating avocado DF subset
avocado = avocado[["Date", "AveragePrice", "Total Volume"]]


# converting Date to timestamp
avocado["Date"] = pd.to_datetime(avocado["Date"])

print(avocado)

# sorting dataframe by date in ascending order
avocado.sort_values(by = "Date", ascending = True, inplace = True)

# creating subplots                 # sharing x axis
myFig, myAxes = plt.subplots(2, 2, sharex = True)
plt.suptitle("Avocado Prices and Volume Time Series")

# creating subplot 1
myAxes[0, 0].scatter(avocado["Date"], avocado["AveragePrice"])
myAxes[0, 0].set_ylabel("Average Price")


# creating subplot 2
myAxes[0, 1].scatter(avocado["Date"], avocado["Total Volume"])
myAxes[0, 1].set_ylabel("Total Volume")

# creating TotalRevenue columns
avocado["TotalRevenue"] = avocado["AveragePrice"]*avocado["Total Volume"]
print(avocado)

# creating new DF
avocado1 = avocado.groupby(by = "Date").sum()
print(avocado1) # average price also summed

# correcting average price
avocado1["AveragePrice"] = avocado1["TotalRevenue"]/avocado1["Total Volume"]
print(avocado1)


# creating subplot 3
myAxes[1, 0].plot(avocado1.index, avocado1["AveragePrice"])
myAxes[1, 0].set_xticklabels(myAxes[1,0].get_xticklabels(), rotation = 90)  # shows warning?
myAxes[1, 0].set_ylabel("Average Price")

# creating subplot 4
myAxes[1, 1].plot(avocado1.index, avocado1["Total Volume"])
myAxes[1, 1].set_xticklabels(myAxes[1,1].get_xticklabels(), rotation = 90)  # shows warning?
myAxes[1, 1].set_ylabel("Total Volume")

# showing plots
plt.show()

# creating smoothed functions
AveragePriceSmooth = avocado1["AveragePrice"].rolling(20).mean()
TotalVolumeSmooth = avocado1["Total Volume"].rolling(20).mean()

# creating smoothed subplot 1
plt.subplot(1, 2, 1)
plt.plot(avocado1.index, AveragePriceSmooth)
plt.xticks(rotation = 90)
plt.ylabel("Average Price")

# creating smoothed subplot 2
plt.subplot(1, 2, 2)
plt.plot(avocado1.index, TotalVolumeSmooth)
plt.xticks(rotation = 90)
plt.ylabel("Total Volume")

# setting title
plt.suptitle("Avocado Prices and Volume Time Series")
plt.show()




