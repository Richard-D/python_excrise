import pandas as pd
obj = pd.Series(["c","a","d","a","a","b","b","c","c"])
print(obj)
uniques = obj.unique()
print("取得唯一值的数组 ",uniques)

count =  obj.value_counts()
print("取得Value的唯一值 ", count)

b = pd.value_counts(obj.values,sort=False)
print("pd.value_counts可用于任何数组或序列")
print(b)

mask = obj.isin(["a","c"])
print(obj[mask])

#
data = pd.DataFrame({"Qu1":[1,3,4,3,4],"Qu2":[2,3,1,2,3],"Qu3":[1,5,2,4,4]})
print(data)
# countD =  data.value_counts()
# print(countD)

print(data.values)
result  = data.apply(pd.value_counts).fillna(0)
print(result)