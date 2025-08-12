#Adding columns

import pandas as pd

emp = {
    "name":["ab","cd","ef","gh","ij","kl","mn"],
    "age":[12,35,67,23,23,56,73],
    "salary":[20000,22000,10000,7000,18000,50000,32000],
    "performance":[85,90,67,89,99,87,100]
}

df = pd.DataFrame(emp)
print(df)

#square brackets df["column_name"] = some_data
df["Bonus"] = df["salary"] * 0.1

#using insert method
#df.insert(location,"column name", data)
df.insert(0,"Emp ID",[10,20,30,40,50,60,70])
print(df)