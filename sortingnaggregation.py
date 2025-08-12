#Sorting data - in rows

import pandas as pd

#SORTING DATA 1 COLUMN - sort_values()
# df.sort_values(by="Column name", True (ascending)/False(Descending), inplace = True)

data = {
    "name" : ["pqr","lmn","xyz","abc"],
    "age" : [13,57,34,29],
    "salary" : [20000,15000,56000,10000]
}

df = pd.DataFrame(data)
print(df)

#Sorting in single column
df.sort_values(by="age",ascending=True,inplace=True)
print(df)

#Sorting in multiple columns
df.sort_values(by=["age","salary"],ascending=[False,False],inplace=True)
print(df)