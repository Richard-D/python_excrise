import numpy as np
from numpy.core.tests.test_mem_overlap import xrange

a= np.arange(10).reshape(2,-1)
print(a)

b = a.copy()

rgb = np.array([[0,0,0],[255,0,0],[0,255,0],[0,0,255],[255,255,255]])

image = np.array([[0,1,2],[3,4,0]])

print(rgb[image])

# 使用矩阵做索引
c = np.arange(12).reshape(3,-1)
print("CC",c)
i = np.array([[0,1],[1,2]])
j = np.array([[2,1],[3,3]])
print(c[:,j])
print("*-----------------")
print(c)
print("i",c[i,:])
print("*-----------------")

# maximum value
time  = np.linspace(20,145,5)
data = np.sin(np.arange(20).reshape(5,-1))
print("Time\n",time)
ind = data.argmax(axis = 0)
time_max = time[ind]
data_max = data[ind, xrange(data.shape[1])]