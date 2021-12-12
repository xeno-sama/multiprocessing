from defs.gradusPlanets import calc as gp
from datetime import date, timedelta
from time import perf_counter
import sqlite3

# создаем таблицу всех планет для нулевых координат

start_time = perf_counter()

try:
    conn = sqlite3.connect('db/ephem.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

# предварительная очистка клиентской таблицы
    cur.execute("delete from tab_0")
    cur.execute("delete from tab_1")

# задаем период для исходной таблицы tab_0
    date_start = date(year=1900, month=1, day=1)
    date_end = date(year=1900, month=1, day=2)

    while date_start <= date_end:
        _natal = [round(i, 2) for i in gp(date_start.year, date_start.month, date_start.day,
                                          12, 0, 0, 0.0, 0.0)]
        dz = tuple([str(date_start)] + _natal)

        cur.execute(f"insert into tab_0 values {dz}")

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

# sun = round(_natal[0], 1)
# moon = round(_natal[1], 1)
# mercury = round(_natal[2], 1)
# venus = round(_natal[3], 1)
# mars = round(_natal[4], 1)
# jupiter = round(_natal[5], 1)
# saturn = round(_natal[6], 1)
# uranus = round(_natal[7], 1)
# neptune = round(_natal[8], 1)
# pluto = round(_natal[9], 1)
