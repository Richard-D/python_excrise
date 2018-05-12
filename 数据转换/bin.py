import pandas as pd
import numpy as np
ages = [20,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100]

cats = pd.cut(ages,bins)
print(cats)
print(type(cats))
print("cat's labels",cats.codes)
count = pd.value_counts(cats)
print(count)
print(type(count))

# 自定义labels
group_names = ["Youth","YoungAdult","MiddleAged","Senior"]
a =  pd.cut(ages,bins,labels=group_names)
print(a)

data = np.random.rand(20)
print(data)
data_cut =  pd.cut(data,4)
print(data_cut)

# 按四分位数进行切割
data_qcut = pd.qcut(data,[0,0.1,0.5,0.9,1.0])
print(pd.value_counts(data_qcut))

