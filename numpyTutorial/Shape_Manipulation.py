import numpy as np
from numpy import newaxis
# 四舍五入
a = np.floor(10*np.random.random((3,4)))
print(a)

print(a.ravel()) # return the array,flattened

# copy
b = a.reshape(6,2)
print(b)

# itself
c = a.resize(6,2)
print(a)

# 转置
print(a.T)

# If a dimension is given as -1 in a reshaping operation,
# the other dimensions are automatically calculated:
d = np.arange(6).reshape(2,-1)
print(d)

# 叠加在一起
e = np.hstack((d,d))
print("水平叠加",e)

f = np.column_stack((d,d))
print("列叠加",e)

g = d[:,newaxis]
print("newaxis",g)

h = np.r_[1:5,0,5,6,9]
print("R_",h)


