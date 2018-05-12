import pandas as pd
import numpy as np
import xlrd

data2 = pd.read_csv("time1.csv",encoding="GBK")
data = pd.read_csv("time.csv",encoding="GBK")
# print(data)
print(type(data))

privoted = data2.pivot("data","name")
print(privoted)
print(type(privoted))