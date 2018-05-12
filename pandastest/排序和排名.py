import numpy as np
import pandas as pd
import pandastest.算术运算和数据对齐 as ss
s = ss.df1
obj = pd.Series(range(4),index=["d","a","b","c"])
print("按index排序 ",obj.sort_index())
print("按列排序 ", obj.sort_values())


print("DataFrame按axis进行排序 ",s.sort_index(axis=0))

frame = pd.DataFrame({"b":[4,7,5,6,],"a":[0,1,0,1]})
print(frame)
print(frame.sort_values(by = ["b","a"]))
print("按多列的value排序")

# 排名
obj = pd.Series([7,-5,7,4,2,0,4])
print(obj.rank())
print("根据出现次数排序\n ",obj.rank(method="first"))

# numpy的argsort是什么？
npp =  np.array([2,5,6,8,8,1])
print(np.argsort(npp))
print(npp)
print("Returns the indices that would sort an array.")
# rank()的破坏平级关系
frame = pd.DataFrame({"b":[4.3,7,-3,2],"a":[0,1,0,1],"c":[-2,5,8,-2.5,]})
print(frame)
print(frame.rank(method="max"))




