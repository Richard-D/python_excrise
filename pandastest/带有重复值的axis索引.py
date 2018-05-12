import pandas as pd
import numpy as np
obj = pd.Series(range(5),index=["a","a","b","b","c"])
print(obj)
print(obj.index.is_unique)
a = obj["a"]
print(a)

df = pd.DataFrame(np.random.randn(4,3),index=["a","a","b","b"])
print(df)
print(df.ix["b"])



