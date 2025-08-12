#grouping 

import pandas as pd

data = {
    "name" : ["pqr","lmn","xyz","abc","hij"],
    "age" : [13,29,34,29,34],
    "salary" : [20000,15000,56000,10000,15000]
}

df = pd.DataFrame(data)
print(df)

grouped = df.groupby("age")["salary"].sum()  #single column
print(grouped)

grouped_multi = df.groupby(["age","name"])["salary"].sum()  #multiple column
print(grouped_multi)