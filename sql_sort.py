import sqlite3


conn = sqlite3.connect('db/test_mp.db')
cur = conn.cursor()

sort = '''create table if not exists temp_table1
AS SELECT *
FROM tab_0
ORDER BY data
'''

cur.execute(sort)

conn.commit()
cur.execute("vacuum")
cur.close()
