import numpy as np
import pandas as pd
data = pd.DataFrame((np.arange(12).reshape(3,-1)),
                    index=["OHIO","COLORADD","NEW YORK"],
                    columns=["one","two","three","four"])
print(data)
data1 = data.rename(index = str.title,columns = str.upper)
print(data1)

# 在原数据修改
_ = data.rename(index = str.title,inplace=True)
print(data)