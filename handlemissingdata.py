#Handling missing data in Pandas

import pandas as pd

#NaN - not a number
#None - for object data types

#is_null() - (True - Nan missing),(False - value present)
emp = {
    "name":["ab",None,"ef","gh","ij","kl","mn"],
    "age":[12,None,67,23,23,56,73],
    "salary":[20000,None,10000,7000,18000,50000,32000],
    "performance":[85,None,67,89,99,87,100]
}

df = pd.DataFrame(emp)
print(df)

print(df.isnull())

#How to drop missing data??
#dropna() - removes missing value from rows (axis =0) and columns (axis = 1)
#df.dropna(axis=0-1, inplace = True)

print(df.dropna(inplace=True))
print(df)

#How to fill up the missing values?
#fillna() - fill the missing values with any value or defaulyt value
#fillna(value,inplace= True)

print(df.fillna(0,inplace=True))  #fills by default value
print(df)

#fills value by any calculated value
df['age'].fillna(df["age"].mean(), inplace=True)
print(df)

#Interpolation - fills value with estimated value on the basis of other values in data in numerical computation
df.interpolate(method="linear",axis=0,inplace=True)
print(df)