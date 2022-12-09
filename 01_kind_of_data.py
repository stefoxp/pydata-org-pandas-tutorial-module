# What kind of data does pandas handle?

import pandas as pd

'''
A DataFrame is a 2-dimensional data structure that
can store data of different types in columns.
It is similar to a spreadsheet, a SQL table
'''
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)

# each column in a DataFrame is a Series
print("Age")
print(df["Age"])

# you can create a Series from scratch
ages = pd.Series([22, 35, 58], name="Ages")

print("Ages")
print(ages)

# a pandas Series has no column labels

print("the maximum Age of the passengers")
print(df["Age"].max())

print("with ages")
print(ages.max())

# the describe() method provides a quick overview
# of the numerical data in a DataFrame
print("describe method")
print(df.describe())
