# 03 select a subset of a DataFrame
import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(titanic.head())

# select columns

print("Age series")
ages = titanic["Age"]

print(ages.head())

print("Age type")
print(type(titanic["Age"]))

print("Age shape")
print(titanic["Age"].shape)

print("select multiple columns")
age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())

print(type(titanic[["Age", "Sex"]]))
print(titanic[["Age", "Sex"]].shape)

# filter specific rows from a DataFrame
above_35 = titanic[titanic["Age"] > 35]

print("above_35 head")
print(above_35.head())

print("above_35 records")
print(titanic["Age"] > 35)

print("above_35 shape")
print(above_35.shape)

class_23 = titanic[titanic["Pclass"].isin([2, 3])]

print("class_23 head")
print(class_23.head())

class_23_f = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]

print("class_23_f head")
print(class_23_f.head())

age_no_na = titanic[titanic["Age"].notna()]

print("age_no_na head")
print(age_no_na.head())

print("age_no_na shape")
print(age_no_na.shape)

# select specific rows and columns from a DataFrame
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

print("adult_names head")
print(adult_names.head())

print("rows 10 till 25 and columns 3 to 5")
print(titanic.iloc[9:25, 2:5])

print("new values assigned to the selected data")
titanic.iloc[0:3, 3] = "anonymous"

print("head")
print(titanic.head())
