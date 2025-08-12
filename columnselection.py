#Selecting specific column - square brackets[] -
#  Series - single column -> column = df["column name"]
#  Dataframes - multiple column --> subset = df[["column1","column2"]]

import pandas as pd

emp = {
    "name":["ab","cd","ef","gh","ij","kl","mn"],
    "age":[12,35,67,23,23,56,73],
    "salary":[20000,22000,10000,7000,18000,50000,32000],
    "performance":[85,90,67,89,99,87,100]
}

df = pd.DataFrame(emp)
print(df)

print(df["name"]) #selecting single column

print(df[["name","age"]])  #selecting multiple columns