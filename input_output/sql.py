import sqlite3
query ="""
CREATE TABLE test
( a VARCHAR(20), b VARCHAR(20),
c REAL, D INTEGER
);
"""
con =sqlite3.connect(":memory:")
con.execute(query)
con.commit()

data = [("A","g",1.25,6),("T","F",2.6,3),("S","C",1.7,5)]
stmt = "INSERT INTO TEST VALUES(?,?,?,?)"

con.executemany(stmt,data)
con.commit()

import pandas.io.sql as sql

z = sql.read_sql("select * from test",con)
print(z)


