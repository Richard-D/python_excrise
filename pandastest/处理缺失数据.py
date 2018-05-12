from numpy import nan as NA
import pandas as pd
import numpy as np
data = pd.Series([1,NA,3.5,NA,7])

a = data.dropna()
print("dropna返回一个仅含非空数据和索引值的Series",a)
b = data[data.notnull()]

# 填充缺失数据
data2 = pd.DataFrame({"one":[1,NA,3,5,NA,7],"two":[1,NA,3,5,NA,7]})
data2.fillna(0)
data3 = data2.fillna({"one":0.5,"two":-1})
print(data3)

print("总是返回被填充对象的引用")
data2.fillna(0,inplace = True)
print(data2)

# 对reindex有效的哪些插值方法也可用于fillna
df= pd.DataFrame((np.random.randn(6,3)))
print(df)
df.ix[2:,1] = NA
df.ix[4:,2] = NA
data4 = df.fillna(method="ffill",limit=2)
print(data4)
