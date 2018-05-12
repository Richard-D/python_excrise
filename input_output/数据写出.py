import csv

import numpy as np
import pandas as pd

data = pd.read_csv("Chapter1.csv",encoding="GBK")

data.to_csv("Out.csv",encoding="GBK")
# 自定义输出
data.to_csv("Self_Out.stdOut",sep="|" ,na_rep="NULL",encoding="GBK")

data.to_csv("sys.stdout",index=False,columns= ["商品名称","进价","供应商"],encoding="GBK")

dates = pd.date_range("1/1/2000",periods = 7)
ts = pd.Series(np.arange(7),index=dates)
ts.to_csv("SeriesCsv.csv",encoding="GBK")

rs = pd.Series.from_csv("SeriesCsv.csv",parse_dates=True)

f = open("Chapter1.csv",encoding="GBK")
reader = csv.reader(f)

# for line in reader:
#     print(line)

lines = list(csv.reader(open("Chapter1.csv",encoding="GBK")))
header,values = lines[0],lines[1:]
data_dict = {h:v for h,v in zip(header,zip(*values))}



class my_dialect(csv.Dialect):
    lineterminator = "\n"
    delimiter = ","
    quotechar = '"'
    quoting = csv.QUOTE_ALL

reader = csv.reader(f,dialect=my_dialect)

for line in reader:
    print(line)

