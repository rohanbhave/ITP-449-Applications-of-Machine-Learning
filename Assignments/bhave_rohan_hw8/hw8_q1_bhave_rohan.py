# Rohan Bhave
# ITP 449
# HW8
# Q1

import pandas as pd
import matplotlib.pyplot as plt

# 1. read dataset into data frame
myDF = pd.read_csv("wineQualityReds.csv")
# pd.set_option('display.max_columns', None)
print(myDF)

# 2. drop Wine from dataframe
myDF.drop(columns="Wine", inplace = True)

# 3. extract quality and store it in separate variable
qualitySeries = myDF["quality"]


# 4. drop quality from dataframe
myDF.drop(columns="quality", inplace = True)

# 5. print DF and Quality
print(myDF)
print(qualitySeries)

# 6. normalize all columns of dataframe
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(myDF)
myDFnorm = pd.DataFrame(scaler.transform(myDF), columns = myDF.columns)

# 7. print normalized DF
print(myDFnorm)

# 8. create range of k values from 1-20 for k means clustering. Iterate and store intertia
from sklearn.cluster import KMeans
inertiaList = []
for k in range (1,21):
    model = KMeans(n_clusters=k, random_state=2023, n_init="auto")
    model.fit(myDFnorm)
    inertiaList.append(model.inertia_)

# 9. plot chart of inertia vs. number of clusters
plt.scatter(range(1, 21), inertiaList)
plt.plot(range(1, 21), inertiaList)
plt.xlabel("Number of Clusters, k")
plt.ylabel("Inertia")
plt.show()

# 10. What cluster would you pick for k-means?
# k = 9 because the inertia doesn't decrease a lot when more clusters are used

# 11. cluster wines into k=6. Assigned cluster to each wine and print
model = KMeans(n_clusters=6, random_state=2023, n_init="auto")
model.fit(myDFnorm)
myDF["cluster"] = model.labels_
print(myDF)

# 12. Add quality  back to dataframe
myDF["quality"] = qualitySeries

# print crosstab of cluster number vs. quality. Comment if clusters represent quality of wine
print(pd.crosstab(myDF["quality"], myDF["cluster"]))
# clusters don't represent quality of wine as all clusters are dominated by 5 or 6

