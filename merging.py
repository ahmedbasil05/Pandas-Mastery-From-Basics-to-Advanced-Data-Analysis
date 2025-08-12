#Merging

import pandas as pd

#df.merge(df1,df2, on ="column name", how=type of join")

df_customers = pd.DataFrame({
    "customer id" : [1,2,3],
    "name" : ["abc","pqr","xyz"]
})

df_orders = pd.DataFrame({
    "customer id" : [1,2,5],
    "order amount" : [250,350,500]
})

merged = pd.merge(df_customers,df_orders,on="customer id",how="cross")
print(merged)