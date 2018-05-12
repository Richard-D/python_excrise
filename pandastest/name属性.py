import pandastest as pd
import numpy as np
obj = pd.Series(np.arange(5),index=("A","B","C","D","E"))
print(obj)
print(obj.name)
obj.name = "testSeriesName"
obj.index.name = "indexName"

