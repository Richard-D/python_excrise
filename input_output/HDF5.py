import pandas as pd


from pandastest.层次化索引 import frame

store = pd.HDFStore("mydata")
store["obj1"] = frame
store["obj1_col"] = frame["a"]

