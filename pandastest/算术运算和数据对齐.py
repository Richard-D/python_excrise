import pandas as pd
import numpy as np

s1 = pd.Series([7.5,-2.5,3.4,1.5],index=["a","b","c","d"])
s2 = pd.Series([-2.1,3.6,-1.5,4,3.1],index=["a","c","e","f","g"])
print("相加\n")
print(s1+s2)
print("在不重叠出引入了NaN值")

df1 = pd.DataFrame(np.arange(9).reshape((3,3)),columns=list("bcd"),
                   index=["Ohio","Texas","Colorado"])
df2 = pd.DataFrame(np.arange(12).reshape((4,3)),columns=list("bde"),
                   index=["Uath","Ohio","Texas","Oregon"])
print(df1)
print(df2)
print(df1 + df2)
print("加法，且有填充值,填充的其实是对应没有的项")
df3 = df1.add(df2,fill_value = 0)
print(df3)
print(df1.add(df2))
