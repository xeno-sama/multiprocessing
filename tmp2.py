from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
import sqlite3
from const import *
from time import perf_counter

lat = [i for i in range(-90, 1, 60)]
lon = [i for i in range(0, 90, 60)]
tmp2 = []
for i in lat:
    for j in lon:
        tmp2.append(f'{i}_{j}')
dx = tuple(tmp2 + ['data'])
print(dx)

# tm = 'test_check'
# start_time = perf_counter()

# try:
#     conn = sqlite3.connect('test_check.db')
#     cur = conn.cursor()
#     print("База данных успешно подключена к SQLite")

# # список всех имен колонок ! для цикла
#     cur.execute("SELECT name FROM PRAGMA_TABLE_INFO('tab_0')")
#     tmp = cur.fetchall()
#     print(tmp[3][0])

#     conn.commit()
#     cur.close()

# except sqlite3.Error as error:
#     print("Ошибка при подключении к sqlite", error)

# finally:
#     if (conn):
#         conn.close()
#         print("Соединение с SQLite закрыто")

# print(f'{(perf_counter() - start_time)}')
