import pandas as pd
df = pd.read_csv("Chapter1.csv",encoding="GBK")
df2 = pd.read_table("Chapter1.csv",sep=",",encoding="GBK")

# 自定义列名
df3 = pd.read_table("Chapter1.csv",sep = ",",names=["商品","供应商","数量","单价"],encoding="GBK")
# print(df3)

parsed = pd.read_csv("Chapter1.csv",index_col=["商品名称","供应商"],encoding="GBK")

skip = pd.read_csv("Chapter1.csv",skiprows=[0,2,3],header=None,encoding="GBK")
print(skip)
