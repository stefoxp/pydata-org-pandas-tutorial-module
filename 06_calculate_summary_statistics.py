# 06 calculate summary statistics

import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(titanic.head())

## Aggregating statistics

print("Average age of the Titanic passengers")
print(titanic["Age"].mean())

print("Median age and ticket fare price")
print(titanic[["Age", "Fare"]].median())

print("describe() function")
print(titanic[["Age", "Fare"]].describe())

print("df.agg() function")
print(titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
))

## Aggregating statistics grouped by category

print("Average age for male versus female")
# split-apply-combine pattern
print(titanic[["Sex", "Age"]].groupby("Sex").mean())

print("without explicit selection of columns")
print(titanic.groupby("Sex").mean(numeric_only=True))

print("with explicit selection of column Age")
print(titanic.groupby("Sex")["Age"].mean())

print("mean ticket fare price for each of the sex and cabin class combinations")
print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean())

## Count number of records by category

print("number of passengers in each of the cabin classes -> value_counts() shortcut")
print(titanic["Pclass"].value_counts())

print("number of passengers in each of the cabin classes -> count()")
print(titanic.groupby("Pclass")["Pclass"].count())
