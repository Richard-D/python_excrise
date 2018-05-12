import xlrd
import pandas as pd
xls_file = pd.ExcelFile("Chapter1.xlsx")

table = xls_file.parse("数据源1")
print(table)
print(type(table))