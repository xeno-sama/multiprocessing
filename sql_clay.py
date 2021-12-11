from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
import sqlite3
from const import *

start = datetime.now()

try:
    conn = sqlite3.connect('test_check.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

    # предварительная очистка клиентской таблицы
    cur.execute("delete from tab_1")

# скопировать из другой базы
    cur.execute("attach database 'test_check_2.db' as ads")
    cur.execute(
        "insert into tab_1(data, moon) select data, moon from ads.tab_2")

# перенести нужное значение из таблицы tab_1 в главную таблицу tab_0
    cur.execute(
        "update tab_0 set moon = tab_1.moon from tab_1 where tab_0.data = tab_1.data")

    conn.commit()
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")

# скопировать в другую базу
# cur.execute("attach database 'ephem03.db' as other")
# cur.execute("insert into other.ephemerides select * from ephemerides")
