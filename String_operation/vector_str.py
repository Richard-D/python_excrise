import pandas as pd
import numpy as np

data = {"Dave":"dava@google,com",
        "Steve":"strve@gmail.com",
        "Rob":"rob@gmail.com",
        "Wes":np.nan}

data = pd.Series(data)
print(data[0:3])

v = data[0:3].values
print("--",type(v))
print(v)
m = []
for x in v:
        print(type(x))
        a = x.split("@")
        print(a)
        m.append(a[0])
print(m)

z = data.get(0)
print(z)

str = data.str[:4]
print(str)
d = data.str.split("@")
print(d)
print(d.str[1])