# 10 manipulate textual data
import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(titanic.head())

print("make all name chars lowercase")
print(titanic["Name"].str.lower())

print("create a new column Surname that contains the surname of the passengers by extracting ...")
print("split(): ", titanic["Name"].str.split(","))

titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
print("Surname: ", titanic["Surname"])

print("extract the passenger data about the countesses on board")
print("contains(): ", titanic["Name"].str.contains("Countess"))
print(titanic[titanic["Name"].str.contains("Countess")])

print("len() method")
print(titanic["Name"].str.len())

print("len().idxmax() method")
print(titanic["Name"].str.len().idxmax())

print("loc() method")
print(titanic.loc[titanic["Name"].str.len().idxmax(), "Name"])

print("replace() method")
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
print(titanic["Sex_short"])
