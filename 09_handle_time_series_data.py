# 09 handle time series data

import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("data/air_quality_no2_long.csv")
air_quality = air_quality.rename(columns={"date.utc": "datetime"})

print(air_quality.head())

print("city unique()")
print(air_quality.city.unique())

## Using pandas datetime properties

print("string to datetime")
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
print(air_quality["datetime"])

"""
pandas.read_csv() and pandas.read_json() can do the transformation to dates
when reading the data using the parse_dates parameter with a list of the columns
"""

print("datetime min and max (pandas.Timestamp)")
print("min: ", air_quality["datetime"].min(), " max: ", air_quality["datetime"].max())
print("max - min (pandas.Timedelta): ", air_quality["datetime"].max() - air_quality["datetime"].min())

print("add a new column containing only the month")
air_quality["month"] = air_quality["datetime"].dt.month
print(air_quality.head())

print("average NO2 concentration for each day of the week of the measurement locations")
print(air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean())

print("plot the typical NO2 pattern during the day of our time series of all station together")
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind="bar", rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")

plt.show()

## Datetime as index
print("air_quality pivot()")
no_2 = air_quality.pivot(index="datetime", columns="location", values="value")
print(no_2.head())

print("get time series properties")
print("year: ", no_2.index.year, " weekday: ", no_2.index.weekday)

print("a plot of the NO2 values in the different stations from the 20th of May till the end of 21st of May")
no_2["2019-05-20":"2019-05-21"].plot()
plt.show()

## Resample a time series to another frequency

print("aggregate the current hourly time series values to the monthly maximum value in each of the stations")
monthly_max = no_2.resample("M").max()
print(monthly_max)

print("the frequency of the time series (freq attribute)")
print(monthly_max.index.freq)

print("a plot of the daily mean NO2 value in each of the stations")
no_2.resample("D").mean().plot(style="-o", figsize=(10, 5))
plt.show()
