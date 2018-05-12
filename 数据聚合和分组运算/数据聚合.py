import numpy as np
import pandas as pd

df = pd.read_csv("Chapter1.csv",encoding="GBK")
# print(df)

# 从groupby数组产生标量值
grouped = df.groupby(["NAME"])["INPUT"].quantile(0.9)
print(grouped)
print(type(grouped))
# 可以看到，grouped是一个Series，GroupBy高效地对Series进行切片，然后对各片调用piece.quanties()

# 我们可以自己定义聚合函数,agg是一个装饰器
def peak_to_peak(arr):
    return arr.max() - arr.min()
groupedBypeak = df.groupby(["NAME"])["INPUT"].agg(peak_to_peak)
print(groupedBypeak)

# 通过聚合运算
df['SUMPRICE'] = df['NUMBER']*df['INPUT']
print(df)

groupedInMulfun = df.groupby(["NAME","BUSSINESS"])
for (k1,k2) in groupedInMulfun:
    print((k1,k2))

groupedInsignfun_mean = groupedInMulfun.agg("mean")
print(groupedInsignfun_mean)

# 传入一组函数与函数名

groupedInMulfun_three = groupedInMulfun.agg(["mean","std",peak_to_peak])
print(groupedInMulfun_three)

# 如果传入的是一个由（name,function）元组组成的列表，则个元素的第一个元素就会被用作DataFrame的列名
groupIntuple = groupedInMulfun.agg([("foo","mean"),("bar",np.std)])
print(groupIntuple)

# 定义一组应用于全部列的函数
functions = ['count','mean','max']
result = groupedInMulfun["SUMPRICE"].agg(functions)
print(result)

# 定义一组不同的函数应用于不同列
function_dict = {"INPUT":np.max,"SUMPRICE":"mean"}
re_group = df.groupby(["NAME"])
print(re_group)
for x in re_group:
    print(x)
re_group_refun = re_group.agg(function_dict)
print(re_group_refun)

# 如何让返回的数据显示出供货商？
# re_group_refun0 = df.groupby(["NAME","BUSSINESS","NUMBER"])
# for (x,y) in re_group_refun0:
#     print((x,y))
# print("-----------------------------------------")
# for m in re_group_refun0:
#     print(m)

