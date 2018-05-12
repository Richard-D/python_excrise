import pandas as pd
import numpy as np
df = pd.DataFrame({"key":["b","b","a","c","a","b"],
                   "data1":range(6)})

d = pd.get_dummies(df["key"])
print(df)
print(d)

values = np.random.rand(10)
bins = [0,0.2,0.4,0.6,0.8,1]
secret = pd.get_dummies(pd.cut(values,bins))
print(secret)