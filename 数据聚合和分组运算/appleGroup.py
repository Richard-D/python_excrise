import pandas as pd
import numpy as np

df = pd.read_csv("Chapter1.csv",encoding="GBK")
def top(df, n = 3, column = "NUMBER"):
    return df.sort_values(by=column)[-n:]

df_top = top(df,3)
print(df_top)


# p = df.groupby("NAME")
# for x in p:
#     print(x)

# top 函数在DataFrame的各个片段上调用，然后由pandas.concat组装到一起
df_apply = df.groupby("BUSSINESS").apply(top)
print(df_apply)

topInput =  df.groupby("BUSSINESS").apply(top,n=1,column = "INPUT")
print(topInput)

# 分位数和桶分析
# pandas有一些能更具指定面元或样本分位数将数据拆分多块的工具
factor = pd.cut(df.INPUT,4)
print(factor)

# 由cut返回的Factor对象可直接用于groupby
def get_input(group):
    return ({'min':group.min(),'max':group.max(),
    'count':group.count(),'mean':group.mean() })

grouped = df.INPUT.groupby(factor)
g = grouped.apply(get_input).unstack()
print(g)

grouping = pd.cut(df.INPUT,10,labels=False)
grouped0 = df.INPUT.groupby(grouping)
gg = grouped0.apply(get_input).unstack()
print(gg)
