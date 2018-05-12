import numpy as np
import pandas as pd
data = pd.Series([1,-999,2,-999,-1000,3],dtype=float)
print(data)
new_data = data.replace(-999,np.nan)
print(new_data)

# 传入字典
new_data2 = data.replace({-999:0,-1000:"wrong"})
print(new_data2)