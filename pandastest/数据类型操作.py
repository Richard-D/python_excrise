# 重新索引
import pandastest as pd
import numpy as np
a = pd.DataFrame(np.array([[1,2],[1,2],[3,4]]))
print(a)
nc = a.columns.delete(0)
ni = a.index.insert(3,3)
print(ni)
nd = a.reindex(index = ni, columns = nc)
print(nd[0])