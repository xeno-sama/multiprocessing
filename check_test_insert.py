from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
from time import perf_counter
import sqlite3
from const import *

start_time = perf_counter()

try:
    conn = sqlite3.connect('test_check.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

# предварительная очистка клиентской таблицы
    cur.execute("delete from tab_0")
    cur.execute("delete from tab_1")

# задаем период для исходной таблицы tab_0
    date_start = date(year=1930, month=1, day=1)
    date_end = date(year=1930, month=1, day=10)
    lat = [i for i in range(-90, 1, 60)]
    lon = [i for i in range(0, 90, 60)]

    while date_start <= date_end:
        tmp = []
        for i in lat:
            for j in lon:
                tmp.append(round(gp(date_start.year, date_start.month, date_start.day,
                                    hour, minutes, tmz, i, j)[1], 2))
        dz = tuple([str(date_start)] + tmp)

        cur.execute("insert into tab_0 values (?,?,?,?,?)", dz)

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

# (data, moon_0_0, moon_0_30, moon_0_60,  moon_0_90)
# , moon_0_120,  moon_0_150, moon_0_180, moon_0_30m,  moon_0_60m, moon_0_90m, moon_0_120m, moon_0_150m, moon_0_180m
#    moon_0_120 = round(gp(date_start.year, date_start.month, date_start.day,
#                          hour, minutes, tmz, 0.0, 120.0)[1], 2)
#    moon_0_150 = round(gp(date_start.year, date_start.month, date_start.day,
#                          hour, minutes, tmz, 0.0, 150.0)[1], 2)
#    moon_0_180 = round(gp(date_start.year, date_start.month, date_start.day,
#                          hour, minutes, tmz, 0.0, 180.0)[1], 2)
#    moon_0_30m = round(gp(date_start.year, date_start.month, date_start.day,
#                          hour, minutes, tmz, 0.0, -30.0)[1], 2)
#    moon_0_60m = round(gp(date_start.year, date_start.month, date_start.day,
#                          hour, minutes, tmz, 0.0, -60.0)[1], 2)
#    moon_0_90m = round(gp(date_start.year, date_start.month, date_start.day,
#                          hour, minutes, tmz, 0.0, -90.0)[1], 2)
#    moon_0_120m = round(gp(date_start.year, date_start.month, date_start.day,
#                           hour, minutes, tmz, 0.0, -120.0)[1], 2)
#    moon_0_150m = round(gp(date_start.year, date_start.month, date_start.day,
#                           hour, minutes, tmz, 0.0, -150.0)[1], 2)
#    moon_0_180m = round(gp(date_start.year, date_start.month, date_start.day,
#                           hour, minutes, tmz, 0.0, -179.9)[1], 2)

# moon_30_0 = round(gp(date_start.year, date_start.month, date_start.day,
#                              hour, minutes, tmz, 30.0, 0.0)[1], 1)
#         moon_30_60 = round(gp(date_start.year, date_start.month, date_start.day,
#                               hour, minutes, tmz, 30.0, 60.0)[1], 1)
#         moon_30_120 = round(gp(date_start.year, date_start.month, date_start.day,
#                                hour, minutes, tmz, 30.0, 120.0)[1], 1)
#         moon_30_180 = round(gp(date_start.year, date_start.month, date_start.day,
#                                hour, minutes, tmz, 30.0, 180.0)[1], 1)
#         moon_30_120m = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, 30.0, -120.0)[1], 1)
#         moon_30_60m = round(gp(date_start.year, date_start.month, date_start.day,
#                                hour, minutes, tmz, 30.0, -60.0)[1], 1)

#         moon_60_0 = round(gp(date_start.year, date_start.month, date_start.day,
#                              hour, minutes, tmz, 60.0, 0.0)[1], 1)
#         moon_60_60 = round(gp(date_start.year, date_start.month, date_start.day,
#                               hour, minutes, tmz, 60.0, 60.0)[1], 1)
#         moon_60_120 = round(gp(date_start.year, date_start.month, date_start.day,
#                             hour, minutes, tmz, 60.0, 120.0)[1], 1)
#         moon_60_180 = round(gp(date_start.year, date_start.month, date_start.day,
#                                hour, minutes, tmz, 60.0, 180.0)[1], 1)
#         moon_60_120m = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, 60.0, -120.0)[1], 1)
#         moon_60_60m = round(gp(date_start.year, date_start.month, date_start.day,
#                                hour, minutes, tmz, 60.0, -60.0)[1], 1)

#         moon_90_0 = round(gp(date_start.year, date_start.month, date_start.day,
#                              hour, minutes, tmz, 90.0, 0.0)[1], 1)
#         moon_90_60 = round(gp(date_start.year, date_start.month, date_start.day,
#                               hour, minutes, tmz, 90.0, 60.0)[1], 1)
#         moon_90_120 = round(gp(date_start.year, date_start.month, date_start.day,
#                                hour, minutes, tmz, 90.0, 120.0)[1], 1)
#         moon_90_180 = round(gp(date_start.year, date_start.month, date_start.day,
#                                hour, minutes, tmz, 90.0, 180.0)[1], 1)
#         moon_90_120m = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, 90.0, -120.0)[1], 1)
#         moon_90_60m = round(gp(date_start.year, date_start.month, date_start.day,
#                                hour, minutes, tmz, 90.0, -60.0)[1], 1)

#         moon_30m_0 = round(gp(date_start.year, date_start.month, date_start.day,
#                               hour, minutes, tmz, -30.0, 0.0)[1], 1)
#         moon_30m_60 = round(gp(date_start.year, date_start.month, date_start.day,
#                                hour, minutes, tmz, -30.0, 60.0)[1], 1)
#         moon_30m_120 = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, -30.0, 120.0)[1], 1)
#         moon_30m_180 = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, -30.0, 180.0)[1], 1)
#         moon_30m_120m = round(gp(date_start.year, date_start.month, date_start.day,
#                                  hour, minutes, tmz, -30.0, -120.0)[1], 1)
#         moon_30m_60m = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, -30.0, -60.0)[1], 1)

#         moon_60m_0 = round(gp(date_start.year, date_start.month, date_start.day,
#                               hour, minutes, tmz, -60.0, 0.0)[1], 1)
#         moon_60m_60 = round(gp(date_start.year, date_start.month, date_start.day,
#                                hour, minutes, tmz, -60.0, 60.0)[1], 1)
#         moon_60m_120 = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, -60.0, 120.0)[1], 1)
#         moon_60m_180 = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, -60.0, 180.0)[1], 1)
#         moon_60m_120m = round(gp(date_start.year, date_start.month, date_start.day,
#                                  hour, minutes, tmz, -60.0, -120.0)[1], 1)
#         moon_60m_60m = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, -60.0, -60.0)[1], 1)

#         moon_90m_0 = round(gp(date_start.year, date_start.month, date_start.day,
#                               hour, minutes, tmz, -90.0, 0.0)[1], 1)
#         moon_90m_60 = round(gp(date_start.year, date_start.month, date_start.day,
#                                hour, minutes, tmz, -90.0, 60.0)[1], 1)
#         moon_90m_120 = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, -90.0, 120.0)[1], 1)
#         moon_90m_180 = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, -90.0, 180.0)[1], 1)
#         moon_90m_120m = round(gp(date_start.year, date_start.month, date_start.day,
#                                  hour, minutes, tmz, -90.0, -120.0)[1], 1)
#         moon_90m_60m = round(gp(date_start.year, date_start.month, date_start.day,
#                                 hour, minutes, tmz, -90.0, -60.0)[1], 1)
