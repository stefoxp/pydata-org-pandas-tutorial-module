# 05 create new columns derived from existing

import pandas as pd

air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)

print("air_quality head")
print(air_quality.head())

print("express the NO2 concentration of the station in London in mg/m3")
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
print(air_quality.head())

print("check the ratio of the values in Paris versus Antwerp and save the result in a new column")
air_quality["ratio_paris_antwerp"] = (air_quality["station_paris"] / air_quality["station_antwerp"])
print(air_quality.head())

print("rename the data columns to the corresponding station identifiers used by OpenAQ")
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
print(air_quality_renamed.head())

print("convert the column names to lowercase")
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
print(air_quality_renamed.head())
