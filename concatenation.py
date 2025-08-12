#Concatenation - merges 2 rows 

import pandas as pd

reg1 = pd.DataFrame({
    "id" : [1,2],
    "name" : ["a","b"]
})

reg2 = pd.DataFrame({
    "id" : [3,4],
    "name" : ["y","z"]
})

con_vertical = pd.concat([reg1,reg2],axis=0,ignore_index=True)
print(con_vertical)