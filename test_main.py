from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
import sqlite3
from const import *

real_data = f'{year_natal}-{month_natal}-{day_natal}'


try:
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

    # cur.execute("delete from tab_0")
    # cur.execute("delete from tab_1")

    conn.commit()
    cur.execute("vacuum")
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")


###########################################

# start = datetime.now()
# end = datetime.now()
# print(end-start)

###########################################

# переписать таблицу с уточнением по луне
# cur.execute("update ephemerides set moon = moon + 10 where moon > 0 ")

# скопировать в другую базу
# cur.execute("attach database 'ephem03.db' as other")
# cur.execute("insert into other.ephemerides select * from ephemerides")

# урезать полную таблицу в краткую, начиная с даты рождения
# cur.execute("delete from ephemerides where date > '2020-02-01' ")

# сжатие базы
# cur.execute("vacuum")

# найти нужнул луну и скопировать ее в начальную moon_0_0 переделать в moon
# lst = func.calc(42, -75)
# df = f'moon_{lst[0]}_{lst[1]}'
# cur.execute(f"update ephemerides set moon_0_0 = {df} ")

###########################################
