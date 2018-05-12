

import pandas as pd
import numpy as np

# 二维ndarray对象
a = pd.DataFrame(np.array([[1,2],[1,2],[3,4]]))
print(a)

b = pd.DataFrame(np.array([[1,2]]))
print(b)

c = pd.DataFrame(pd.Series(25,index=["a","b","c"]))
print(c)

# 等长列表
l1 = {"one ":[1,2,3,4],"two":[9,8,7,6]}
d = pd.DataFrame(l1)
print(d)

# 通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series
Data = {
    "year":[2000,2001,2002,2001,2002],
    "state":["ohio","ohio","ohio","Nevada","Nevada"],
    "pop":[1.5,1.7,3.6,2.4,2.9]
}
frame2 = pd.DataFrame(Data,columns=["year","state","pop","debt"],
             index = ["one","two","three","four","five"])
print("frame:\n",frame2)

#通过类似字典标记的方式或属性的方式
print(frame2["state"])
print(frame2.year)
print("可以看到：Name属性被设置为字典标记")

# 获取位置或名称获取行
print(frame2.ix["three"])
print("利用索引字段ix获取行")

frame2["debt"] = [16.5,17.6,14.3,25.6,11.2]
print(frame2)

frame2["debt"] = np.arange(5)
print(frame2)

# 创建一个不存在的新列
frame2["eastern"] = frame2.state == "ohio"
print(frame2)

frame2["eastern"].name = "east"
del frame2["eastern"]
print(frame2)
print("创建了一个bool序列，del一个clumns")

# 另一种常见的数据形式就是嵌套字典
pop = {"Nevada":{2001:2.4,2002:2.9},
       "Ohio":{2000:1.5,2001:1.7,2002:3.6}}

frame3 = pd.DataFrame(pop)
print(frame3)
print("外键做为columns,内键的key作为行，如果指定了index就不准守这条规则")

print("转置:",frame3.T)

# 设置了DataFrame的index和columns的name属性，则这些信息也会被显示出来
frame3.index.name= "year"
frame3.columns.name = "state"
print(frame3)

print(frame3.values)
print("返回一个ndarry")
print(frame2.values,frame2.values.dtype)


# 二维ndarry
print("二维ndarry：",pd.DataFrame([[1,2],[2,3]],index=["one","two"])) #列表 作为行
print("字典: ",pd.DataFrame({"onw":[1,2],"two":[3,4]},index=["one","two"])) #字典 作为列
print(pd.Series([1,2,3,4],[5,6,7,8]))
s = pd.Series(np.arange(10))
print(s)
print("-------------")
print("Series:", pd.DataFrame([s],index =["行"])) # 列表，作为行
print(pd.DataFrame(s,columns=["列"])) # 字典，作为列
print("区分【】 列表  与  字典")



