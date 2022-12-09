# 02 read and write tabular data

import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print("titanic.csv")
print(titanic)

print("the first 8 rows (head method)")
print(titanic.head(8))

print("columns data types")
print(titanic.dtypes)

print("to Excel conversion (require openpyxl module)")
titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)
titanic_ex = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")

print("head()")
print(titanic_ex.head())

print("info()")
print(titanic_ex.info())
