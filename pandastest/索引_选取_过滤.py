import pandas as pd
import numpy as np
import pandastest.重新索引 as pdd
obj = pd.Series(np.arange(4),index=["a","b","c","d"])
print("数字索引： ",obj[3])
print("索引对象索引: ",obj["d"])
print("切片索引",obj[1:])
print("注意切片索引/参数永远都是对应着行的")
print("因此我们可以得知，pandas有一个默认数字索引与自定义索引，两者不能混用")

print("pandas索引是包含末端的： ",obj[1:2])
print(pdd.frame)
print("DataFrame索引默认是对axis = 1的" ,pdd.frame["ohio"])
print("如果我要按行索引呢?")
print(pdd.frame[1:])
#print(pdd.frame2[2]) #这样索引是错误的，为什么？
print("BINGO")
print("满足条件所在的一行",pdd.frame[pdd.frame["Texas"]>5])
print("上述的从形式上可以=： ",pdd.frame[-1:])
pdd.frame[pdd.frame<5] = 0
print(pdd.frame)
print("赋值操作时在原DataFrame上进行，所以。。。")

a = pdd.frame
b = a.ix["a",["one","two","three"]]
print(b)
print("注意列不一样的时候，此时b的value都为NaN")
print(pdd.frame.ix[["c","a"],["ohio","Texas" ,"California"]])
print("这样才是查找子集的正确方式")
print(a.ix["a",[0,1,2]])
print("对一行进行ix，自动转化为Series,因为DataFrame本就可以看成Name作为Index的Series组")

c = a.ix[2]
print("作者为了避免frame[:,col]，将所有的标签索引放在了ix里")
# d = a.ix[1:]
print("------------")
print(a.ix["a"]<5)
print("根据列定位行")
print(a.ix[a.ohio==0])
print(a)
print("根据行定位列")
print("第一种方法")
g = a.T
print(g)
print(g.ix[g.b ==5])
print("第二种方法，没想出来")
print(a["ohio"] ,"\n==",a.ohio,"\n==",a.ix[:,0])






