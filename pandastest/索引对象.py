import pandas as pd
import numpy as np
import pandastest.CreateDateFrame as cs
# pandas的索引对象负责管理轴标签和其他元数据
obj =pd.Series(range(3),index = ["a","b","c"])
index = obj.index
print(index)
print("Index对象是不可修改的，因此用户不能对其进行修改")
obj["a"] = 5
print(obj)
print("思考一下，不可变的特性/好处。为什么索引是不可变的？")

# 既然索引是对象，那么必然有一些自己的方法和属性
print(cs.frame3)
print(cs.frame2)
print(cs.frame3.index.append(cs.frame2.index))
print("连接两个index")

