from defs.gradusPlanets import calc as gp
from datetime import date, timedelta
from time import perf_counter
import sqlite3
# создаем таблицу всех координат луны

start_time = perf_counter()

try:
    conn = sqlite3.connect('db/ephem_allmoons.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

# предварительная очистка клиентской таблицы
    cur.execute("delete from tab_0")

# задаем период для исходной таблицы tab_0
    date_start = date(year=1900, month=1, day=1)
    date_end = date(year=1900, month=2, day=1)
    lat = [i for i in range(-90, 91, 10)]
    lon = [i for i in range(-180, 181, 10)]

    while date_start <= date_end:
        tmp = []
        for i in lat:
            for j in lon:
                tmp.append(round(gp(date_start.year, date_start.month, date_start.day,
                                    0, 0, 0, i, j)[1], 2))
        dz = tuple(tmp + [str(date_start)])

        cur.execute(
            f"insert into tab_0 values {dz}")

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

print(f'{(perf_counter() - start_time)}')
