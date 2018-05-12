import pandas as pd
import numpy as np
data = pd.Series(np.random.randn(10),
                 index = [["a","a","a","b","b","b","c","c","d","d"],
                          [1,2,3,1,2,3,1,2,2,3]])
print(data)
# 这个是怎么对应起来的...
print(data.index)

data2 = pd.Series(np.random.randn(10),
                 index = [[0, 0, 0, 1, 1, 1, 2, 2, 3, 3], [0, 1, 2, 0, 1, 2, 0, 1, 1, 2]])
print(data2)

# 操作多维对象的子集
print(data["b"])

print(data["b"][1])

# 是否可以切片
print("data\n",data)
print(data["b":"c"])

print(data[:,3])

# 我想知道里层索引分片
print(data[3:]) # 按最里层
print(data.ix[0:6] == data[0:6])
print(data.ix[["a","b","c"][0:2]] == data[0:6])
print("看来一定要把颗粒度定在第二维才能分片，即，不能批量分片")
print(data["b"][0:2])
print("但是可以直接在内层中选取")
print(data[:,2])

data2 =  data.unstack()
print(data2)
frame  = pd.DataFrame(np.arange(12).reshape((4,3)),
                      index = [["a","a","b","b"],[1,2,2,1]],
                      columns = [["Ohio","Ohio","Colorado"],
                      ["Green","Red","Green"]])

print(frame)
print("只看a\n",frame.ix["a"])
print("只看前X行\n",frame.ix[0:2] == frame[0:2])
print("只看某列分片\n",frame.ix[:,0:1])
print("只看某列自定义索引", frame["Ohio"])
print("是否可以符合索引",frame[0:2]["Ohio"])
print("Green",frame["Ohio"][["Green","Red"]])

print(frame.ix["a"][0:1])
print("终极定位")
print(frame.ix["a"][0:1]["Ohio"]["Green"])

# 重排分级顺序
print(frame.sort_index(0))
print(frame.index)
print(frame.sort_index(0,1).sort_index(0))

# 


