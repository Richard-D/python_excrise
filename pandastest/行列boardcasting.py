import numpy as np
import pandas as pd
import pandastest.算术运算和数据对齐 as ss
arr = np.arange(12.).reshape((3,-1))
print(arr)

print("broadcasting: " ,arr-arr[0])
print("实际上是新增了两列0")
frame = ss.df1
series = frame.ix[0]
print(frame-series)

series3 = frame["d"]
print(frame.sub(series3,axis=0))
print("使用算术运算方法可以在列上boardcasting")
