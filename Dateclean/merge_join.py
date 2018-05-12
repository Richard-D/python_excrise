# 按索引。列名 行名合并
import pandas as pd
df1 = pd.DataFrame({'key':['b','b','a','a','d','d','a'],
                'data':range(7)})

df2 = pd.DataFrame({'key':['a','b','d'],
                    'data2':range(3)})

print(df1)
print(df2)
print("merge之后会是怎么样？")
df_merge =  pd.merge(df1,df2,on="key")
print(df_merge)
print("重叠key")

df3 = pd.DataFrame({'lkey':['c','b','a','a','d','d','a'],
                'data':range(7)})

df4 = pd.DataFrame({'rkey':['f','b','d'],
                    'data2':range(3)})
df_meger1 = pd.merge(df3,df4,left_on='lkey',right_on='rkey')
print(df_meger1)
print("默认inner内连接")

df_meger_outer = pd.merge(df3,df4,how='right',left_on="lkey",right_on="rkey")
print(df_meger_outer)

print("在进行列列连接时，DateFrame中的索引会被丢弃")

# 对于层次化索引
import numpy as np
lefth = pd.DataFrame({"key1":['Ohio','Ohio','Ohio','Nevada'],
                      "key2":[2000,2001,2002,2001],
                      "data":np.arange(4.)})

righth = pd.DataFrame(np.arange(12).reshape((6,2)),
                      index = [["Nevada","Ohio","Ohio","Nevada","Ohio","Ohio"],
                      [2001,2000,2000,2000,2001,2002]],
                      columns=["event1","event2"])
print(righth)
print(lefth)
print("这种形势，你必须以列表的形式指明用作合并键的多个列")
pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True)

left2 = pd.DataFrame([[1.,2.],[3.,4.],[5.,6.]],index=["a","b","c"],columns=["Ohio","Nevada"])
print(left2)
right2 = pd.DataFrame([[7.,8.],[9.,10.],[11.,12.],[13.,14.]],index=["b","c","d","e"],columns=["Missouri","Alabama"])
print(right2)

merger_index = pd.merge(left2,right2,how="outer",left_index=True,right_index=True)
merger_index1 = left2.join(right2,how="outer")
print(merger_index)
print(merger_index1)

merger_index2 =  lefth.join(righth,on=["key1","key2"])
print(merger_index2)