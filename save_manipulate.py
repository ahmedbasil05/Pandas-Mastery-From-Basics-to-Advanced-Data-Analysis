#Save manipulated data

import pandas as pd

#Creating own dataframe and saving it
data = {
    "name":["abc","xyz","pqr"],
    "age" : [10,20,30],
    "city" : ["isb","rwp","lhr"]
}

df = pd.DataFrame(data)  #convert to Dataframe
print(df)

#saving to CSV
df.to_csv("output",index=False)

#saving to JSON
df.to_json("output.json")

#saving to Excel
df.to_excel("output.xlsx")


