import numpy as np
a = np.arange(100).reshape(5,20)
np.savetxt('a.csv',a,fmt='%d',delimiter=",")

# 读入csv
b = np.loadtxt("a.csv",delimiter=",")
print(b)

# 只能存储一维和二维数据
