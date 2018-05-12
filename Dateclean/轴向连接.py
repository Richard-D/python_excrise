# 按照轴进行内连接、左连接与右连接
import numpy as np
import pandas as pd

arr = np.arange(12).reshape((3,4))
print(arr)
arr_con = np.concatenate([arr,arr],axis=1)
print(arr_con)


left2 = pd.DataFrame([[1.,2.],[3.,4.],[5.,6.]],index=["a","b","c"],columns=["Ohio","Nevada"])
right2 = pd.DataFrame([[7.,8.],[9.,10.],[11.,12.],[13.,14.]],index=["b","c","d","e"],columns=["Missouri","Alabama"])

s1 = pd.concat([left2,right2],axis=0)
print(s1)
# s2 = pd.concat([left2,right2],axis=1,join_axes=[["a","b","c","d","e"]])
# print(s2)

result = pd.concat([left2,right2],axis=1, keys = ["one","two"],join="inner")
print(result)