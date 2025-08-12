#DATA Exploration - Quick Overview

#dealing with row

import pandas as pd
df2 = pd.read_json("sample_boston_data.json")
print("\nJSON Data:\n", df2)

print("display first 2 rows ")
print(df2.head(2))

print("display last 2 rows")
print(df2.tail(2))

#displaying the info of dataset - Summarizing 
#---> solution of problem?
#         1- no of rows and columns?
#         2- datatype?
#         3- missing values

print(df2.info())

