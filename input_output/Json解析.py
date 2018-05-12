import json

from pandas import DataFrame, Series

with open("json","r") as js:
    result = json.load(js)

siblings = DataFrame(result["data"])
a = Series(result["data"])
print(a)