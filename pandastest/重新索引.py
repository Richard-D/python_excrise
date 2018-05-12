import pandas as pd
import numpy as np
#reindex,创建一个适应新索引的新对象
obj = pd.Series([4.5,7.2,-5.3,3.6],index=["a","b","c","d"])
obj2 = obj.reindex(["a","b","c","d","e"])
print(obj2)
print("虽然index对象不可变，但是我们可以使用reindex重新索引")

obj3 = pd.Series(["blue","purple","yellow"],index=[0,2,4])
obj4 =  obj3.reindex(range(6),method= "ffill")
print(obj3)
print("可以看出reindex是重新生成了一个Series",obj4)
# 我们需要更精准的插值方式。类比成excel

frame = pd.DataFrame(np.arange(9).reshape((3,3)),index=["a","b","c"],
                     columns = ["ohio","Texas","California"])

print(frame)
frame2 = frame.ix[["a","b","c","d"],["Texas","Utah","California"]]
print(frame2)

# 丢弃指定轴上的项
new_obj = obj.drop("a")
print(new_obj)
print(obj)

# 索引、选取和过滤
obj = pd.Series(np.arange(4),index=["a","b","c","d"])
print(obj)
print(obj["c":"d"])
print(obj[0])
