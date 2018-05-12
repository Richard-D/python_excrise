import pandastest.算术运算和数据对齐 as ss
import pandas as pd
print(ss.df1)
s = ss.df1

print("numpy的ufuncs也可用于操作pandas对象")
f = lambda x:x.max()-x.min()
print("最大-最小",s.max() - s.min())
a = ss.df1.apply(f)
print(a)
print("许多最为常见的数组统计功能都被实现成DataFrane的方法")

def f(x):
    return pd.Series([x.min(),x.max()],index=["min","max"])

print(ss.df1.apply(f))

# 元素级的Python函数
format = lambda x:"%.2f" %x
b  =  s.applymap(format)
print(b)

