# Rohan Bhave
# ITP 449
# HW5
# Q3

import pandas as pd
import matplotlib.pyplot as plt

# reading csv files
dailyDF = pd.read_csv("03-04-2023.csv")
confirmedDF = pd.read_csv("time_series_covid19_confirmed_US.csv")
deathsDF = pd.read_csv("time_series_covid19_deaths_US.csv")

# 1
# state with highest number of deaths
highest_deaths = dailyDF[["Province_State", "Deaths"]].sort_values(by="Deaths", ascending=False).head(1)
print("Highest number of deaths:\n", highest_deaths["Province_State"])
print()

# 2
# 2nd lowest incident rate
second_lowest_incident = dailyDF[["Province_State", "Incident_Rate"]].sort_values(by="Incident_Rate").iloc[1]
print("Second lowest incident rate:\n", second_lowest_incident)
print()

# 3
# state with highest case fatality ratio
highest_ratio = dailyDF[["Province_State", "Case_Fatality_Ratio"]].sort_values(by="Case_Fatality_Ratio").tail(1)
print("Highest ratio:\n", highest_ratio["Province_State"])
print()

# state with lowest case fatality ratio
lowest_ratio = dailyDF[["Province_State", "Case_Fatality_Ratio"]].sort_values(by="Case_Fatality_Ratio").head(1)
print("Lowest ratio:\n", lowest_ratio["Province_State"])
print()

# difference in ratios
print("Difference in ratios:")
print(float(highest_ratio["Case_Fatality_Ratio"]) - float(lowest_ratio["Case_Fatality_Ratio"]))

# 4
# daily new cases for top 5 highest confirmed cases
grouped_states_cases = confirmedDF.groupby("Province_State").sum(numeric_only=True)
top_5_states = grouped_states_cases.iloc[:,-1].sort_values(ascending=False).head().index

# getting transposed DF for top 5 states
top_5_confirmedDF = grouped_states_cases.loc[top_5_states, "1/22/20":"3/4/23"].transpose()


# plotting confirmed cases
myfig = plt.figure()
ax1 = myfig.add_subplot(1,2,1)
ax1.plot(top_5_confirmedDF)
ax1.legend(top_5_confirmedDF.columns)
ax1.set_title("Daily Confirmed Cases in Top 5 Affected States", size=10)
plt.xticks(["3/1/20", "9/1/20", "3/1/21", "9/1/21", "3/1/22", "9/1/22", "3/1/23"])

# 5
# daily deaths for top 5 highest confirmed cases
grouped_states_deaths = deathsDF.groupby("Province_State").sum(numeric_only=True)
top_5_deathsDF = grouped_states_deaths.loc[top_5_states, "1/22/20":"3/4/23"].transpose()

# plotting daily deaths
ax2 = myfig.add_subplot(1,2,2)
ax2.plot(top_5_deathsDF)
ax2.legend(top_5_deathsDF.columns)
plt.xticks(["3/1/20", "9/1/20", "3/1/21", "9/1/21", "3/1/22", "9/1/22", "3/1/23"])
ax2.set_title("Daily Deaths in Top 5 Affected States", size=10)

# showing plots
plt.show()