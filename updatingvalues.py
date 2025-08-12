#Updating the Values
import pandas as pd

#.loc[] - updates a value at specific row and column
#df.loc[index,"Column name"] = new_value

emp = {
    "name":["ab","cd","ef","gh","ij","kl","mn"],
    "age":[12,35,67,23,23,56,73],
    "salary":[20000,22000,10000,7000,18000,50000,32000],
    "performance":[85,90,67,89,99,87,100]
}

df = pd.DataFrame(emp)
print(df)

df.loc[3,"salary"] = 17000
print(df)


#updating whole 
df["salary"] = df["salary"] * 1.05
print(df)
