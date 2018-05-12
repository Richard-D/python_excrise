import pandas as pd
import numpy as np
chunker = pd.read_csv("Chapter1.csv",chunksize=100,encoding="GBK")
tot = pd.Series([])
for x in chunker:
    tot = tot.add(x["商品名称"].value_counts())
print(chunker)
print(tot)