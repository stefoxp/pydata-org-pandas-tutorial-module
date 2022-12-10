# 04 create plots in pandas

import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)

print("air_quality head")
print(air_quality.head())

# with a DataFrame, pandas creates by default one line plot for each of the columns with numeric data
print("plot")
print(air_quality.plot())
plt.show()

print("plot only the columns of the data with the data from Paris")
air_quality["station_paris"].plot()
plt.show()

print("compare the NO2 values measured in London versus Paris")
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

print("alternative type of plot available")
print([method_name for method_name in dir(air_quality.plot) if not method_name.startswith("_")])

print("box plot sample")
air_quality.plot.box()
plt.show()

print("separate subplot for each of the columns")
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()

print("customize, extend or save the resulting plot")

# create an empty Matplotlib Figure and Axes
fig, axs = plt.subplots(figsize=(12, 4))
# Use pandas to put the area plot on the prepared Figure/Axes 
air_quality.plot.area(ax=axs)
# Do any Matplotlib customization you like
axs.set_ylabel("NO$_2$ concentration")
# Save the Figure/Axes using the existing Matplotlib method
fig.savefig("data/no2_concentrations.png")

plt.show()

