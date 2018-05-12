# 聚合能将一维数组化为标量值，transform和apply方法能执行更多其他的分组运算

import pandas as pd
import numpy as np

df = pd.read_csv("Chapter1.csv",encoding="GBK")
print(df)

k1_means = df.groupby(["NAME"]).mean().add_prefix("mean_")
print(k1_means)

df_merge = pd.merge(df,k1_means,left_on="NAME",right_index=True)
print(df_merge)

def demean(arr):
    return arr - arr.mean()

demeaned = df.groupby("BUSSINESS").transform(np.mean)
print(demeaned)


