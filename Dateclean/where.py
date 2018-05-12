# 合并重叠数据
import numpy as np
import pandas as pd

a = pd.Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],
              index=["f","e","d","c","b","a"])
b= pd.Series(np.arange(len(a),dtype=np.float64),
              index=["f","a","d","c","b","a"])
print(a)
print(b)
# 索引部分重叠的两个数据集
c = np.where(pd.isnull(a),b,a)
print(c)

d = b[:-2].combine_first(a[2:])
print(d)


