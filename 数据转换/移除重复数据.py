import numpy as np
import pandas as pd

data = pd.DataFrame({"k1":["one"]*3 + ["two"] *4,
                     "k2":[1,1,2,3,3,4,4]})

print(data)

# 判断是否重行
print(data.duplicated())
a = data.drop_duplicates()
print(a)

# 多列
data["k4"] = range(7)
print(data)
print(data.drop_duplicates(["k1"]))

