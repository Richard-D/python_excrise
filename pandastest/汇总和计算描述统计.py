# pandas对象拥有一组常用的数学和统计方法，它们大部分都属于
#约简和汇总统计，用于从Series中提取单个值或从DataFrame的行列中
#提取一个Series
import pandas.io.data as web
from pandastest import 算术运算和数据对齐 as cd
a  = cd.df3
print(cd.df3)
# 调用DataFrame的sum方法会返回一个含有小计的Series
print(cd.df3.sum())
print(a.sum(axis = 1))

#有些方法是间接统计（即返回索引这一类）
print(a.idxmax())
print("这个就是返回列对应的最大的那一行的索引")

#另一种方法则是累计型的：
print(a.cumsum())
print(a)





