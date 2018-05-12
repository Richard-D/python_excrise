import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(6).reshape((2,3)),
                    index=pd.Index(["ohio","Colorado"],name="state"),
                    columns=pd.Index(["one","two","three"],name= "number"))
print(data)
result = data.stack()
print(result)
print("转化为了层次化的Series")

result.unstack()
print("重排为DataFrame")

s1 = pd.Series([0,1,2,3],index=["a","b","c","d"])
s2 = pd.Series([4,5,6],index=["c","d","e"])

data2 = pd.concat([s1,s2],keys = ["one","two"])
print(data2)
print(data2.unstack())

df = pd.DataFrame({"left":result,"right":result+5},
                  columns = pd.Index(['left','right'],name="side"))
print(df)
#相当于行筛选、列筛选print(df.unstack("state"))
print(df.unstack("number"))
print(df.stack("side"))