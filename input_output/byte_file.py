import pandas as pd
frame = pd.read_csv("Chapter1.csv",encoding="GBK")
print(frame)

obj = {"name":1}
# frame.to_pickle(obj)
# pd.read_pickle("Chapter.csv")