import pandas as pd
import numpy as np
a = pd.Series([9,8,7,6])
print(a)


# 五种生成Series的方法
a_ = pd.Series(25)
b_ = pd.Series({"a":9,"b":10,"c":20})
c_ = pd.Series(np.arange(5))
d_ = pd.Series(range(5))
print(type(range(5)))
print( "--",d_)


# 从标量创建
b = pd.Series(25,index=["a","b","c"])

# 从字典
c = pd.Series({"a":9,"b":10,"c":11})
d = pd.Series({"a":9,"b":10,"c":11},index=["c"])
print(d)

#从ndarray
n = pd.Series(np.arange(5),index=np.arange(9,4,-1))

# range
f = pd.Series(range(5))
print(f)
print(f.values)