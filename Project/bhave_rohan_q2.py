# Rohan Bhave
# ITP 449
# Project
# Q2

import pandas as pd

# A. loading data set
myDF = pd.read_csv("Stores.csv")

# extracting Store column
stores = myDF["Store"]

# dropping Stores from dataframe
myDF.drop(columns="Store", inplace = True)

# Standardizing data set
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(myDF)   # scaling features
myDFnorm = pd.DataFrame(data=scaler.transform(myDF), columns = myDF.columns)

# B. running k-means for k 1-10
from sklearn.cluster import KMeans
inertiaList = []
for k in range (1,11):
    model = KMeans(n_clusters=k, random_state=2023, n_init="auto")
    model.fit(myDFnorm)
    inertiaList.append(model.inertia_)

# C. plotting inertias vs k
import matplotlib.pyplot as plt
plt.scatter(range(1, 11), inertiaList)
plt.plot(range(1, 11), inertiaList)
plt.xlabel("Number of Clusters, k")
plt.ylabel("Inertia")
plt.show()

# D. best k
# k = 6

# E. what cluster does Seattle score belong to
seattle = [[6.3, 3.5, 2.4, 0.5]] # np array with data
seattle_scaled = pd.DataFrame(data=scaler.transform(seattle), columns = myDF.columns)
model = KMeans(n_clusters=6, random_state=2023, n_init="auto")
model.fit(myDFnorm)
seattle_pred = model.predict(seattle_scaled)
print("Seattle cluster:", seattle_pred)

# F. Adding store and cluster columns to original dataframe
myDF["Store"] = stores
myDF["cluster"] = model.labels_
print(myDF)

# G. histogram of clusters
import seaborn as sn
sn.countplot(myDF, x="cluster")
plt.show()



