from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
import sqlite3
from const import *
from time import perf_counter


try:
    conn = sqlite3.connect('db/ephem.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

    cur.execute("attach database 'db/moons/moon_0_0.db' as ads")

    cur.execute("select name from ads.PRAGMA_TABLE_INFO('tab_0')")
    list_colnames = [i[0] for i in cur.fetchall()]
    print(list_colnames)

    conn.commit()
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")
