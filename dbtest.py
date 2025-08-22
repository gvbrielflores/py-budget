import sqlite3 as sq
con = sq.connect("pybudget.db")

cursor = con.cursor()

res = cursor.execute("select * from income_streams;")

print(res.fetchall())