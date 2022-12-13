# 07 reshape layout of tables

import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("data/titanic.csv")
air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)

print("titanic head")
print(titanic.head())
print("air_quality head")
print(air_quality.head())

## Sort table rows

print("sort the Titanic data according to the age of the passengers")
print(titanic.sort_values(by="Age").head())

print("sort the Titanic data according to the cabin class and age in descending order")
print(titanic.sort_values(by=["Pclass", "Age"], ascending=False).head())

## Long to wide table format

# filter for no2 data only
no2 = air_quality[air_quality["parameter"] == "no2"]

# use 2 measurements (head) for each location (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)

print("no2_subset")
print(no2_subset)

print("values for the three stations as separate columns next to each other")
print(no2_subset.pivot(columns="location", values="value"))

print("no2 head")
print(no2.head())

print("no2.pivot().plot()")
no2.pivot(columns="location", values="value").plot()

plt.show()

# Pivot table

print("mean concentrations for NO2 and PM2.5 in each of the stations in table form")
print(air_quality.pivot_table(values="value", index="location", columns="parameter", aggfunc="mean"))

print("same pivot with subtotals (margins)")
print(air_quality.pivot_table(values="value", index="location", columns="parameter", aggfunc="mean", margins=True))

# Wide to long format

print("no2 with new index")
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()
print(no2_pivoted.head())

print("collect all air quality NO2 measurements in a single column")
no_2 = no2_pivoted.melt(id_vars="date.utc")
print(no_2.head())

print("pandas.melt() parameters")
no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name="id_location",
)
print(no_2.head())
