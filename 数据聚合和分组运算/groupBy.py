import pandas as pd
import numpy as np

df = pd.read_csv("Chapter1.csv",encoding="GBK")
# 根据name调用groupby

grouped = df["INPUT"].groupby([df["BUSSINESS"],df["NAME"]])
print(grouped)

print(grouped.mean())

a = df[["NAME","BUSSINESS"]]
print(a)

# 可以将列名（字符串、数字、其他Python对象）、数组用作分组键
gp = df.groupby("NAME").mean()
print(gp)

# 用到GroupBy的size方法:数量
size = df.groupby(["BUSSINESS","NAME"]).size()
print(size)

# 对分组进行迭代
print("--------------------------------------")
for name,group in df.groupby("NAME"):
    print(group)

print("--------------------------------------")
for (k1,k2),group in df.groupby(["NAME","BUSSINESS"]):
    print((k1,k2))
    print(group)

print("--------------------------------------")
# 将数据片段做成一个字典
pieces = dict(list(df.groupby("NAME")))
print(pieces)

# 根据dtype对列进行分组
print(df.dtypes)
groupBycol = df.groupby(df.dtypes,axis=1)
print(dict(list(groupBycol)))

# 选取一个或一组列
# 这种索引操作所返回的对象是一个已分组的DataFrame(如果传入的列表或数组)，
# 或者已分组的Series
print("-------")
GroupNumberbyNAME  = df.groupby("NAME")[["NUMBER"]]
print(GroupNumberbyNAME)
#<pandas.core.groupby.DataFrameGroupBy object at 0x03EF8F10>
for x in GroupNumberbyNAME:
    print(x)

print("--------")
GroupInputMeanByName = df.groupby("NAME")[["INPUT"]].mean()
print(GroupInputMeanByName)



# 通过字典或者Series进行分组
people = pd.DataFrame(np.random.randn(5,5),
                      columns = ["a","b","c","d","e"],
                      index=["Job","Steve","Wes","Jim","Trvis"])
people.ix[2:4,["b","c"]] = np.nan
print(people)

mapping = {"a":"red","b":"red","c":"blue","d":"blue","e":"orange","f":"red"}
# 按列叠加
by_columns = people.groupby(mapping,axis=1).sum()
print(by_columns)
# 使用Series作为分组键
map_series = pd.Series(mapping)
by_columns_with_Series = people.groupby(map_series,axis=1).sum()
print(by_columns_with_Series)

# 通过函数进行分组
# 相较于字典或Series，Python函数在定义分组映射关系时可以更有创意且更为抽象
GroupByNamelen = people.groupby(len).sum()
print(GroupByNamelen)

# 根据索引级别分组
columns  = pd.MultiIndex.from_arrays([["US","US","US","JP","JP"],
                                     [1,3,5,1,3]],names=["cty","tenor"])
hier_df = pd.DataFrame(np.random.randn(5,5),index=[["one","two","three","four","five"],[1,2,3,4,5]],columns=columns)
print(hier_df)
GroupByCty  = hier_df.groupby(level="cty",axis=1).count()
print(GroupByCty)

