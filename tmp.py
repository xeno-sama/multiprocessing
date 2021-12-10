from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
import sqlite3
from const import *

start = datetime.now()

try:
    conn = sqlite3.connect('test_check_2.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

# очистка таблиц
    cur.execute(''' drop table if exists tab_2 ''')
# предварительная очистка клиентской таблицы
    # cur.execute("delete from tab_2")

    create_tab_2 = ''' create table tab_2 (
        data text,
        moon real
    );
    '''

    cur.execute(create_tab_2)

# задаем период для исходной таблицы tab_0
    date_start = date(year=1930, month=1, day=1)
    date_end = date(year=1930, month=1, day=10)

    while date_start <= date_end:
        tmp = []
        tmp.append(round(gp(date_start.year, date_start.month, date_start.day,
                            hour, minutes, tmz, 70, 70)[1], 2))
        dz = tuple([str(date_start)] + tmp)

        cur.execute("insert into tab_2 values (?,?)", dz)

        print(date_start)  # видеть лог
        date_start += timedelta(days=1)

    conn.commit()
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")

end = datetime.now()
print(end-start)
