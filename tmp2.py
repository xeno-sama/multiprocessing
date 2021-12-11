from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
import sqlite3
from const import *
from time import perf_counter
from multiprocessing import Pool, Process, Lock
import multiprocessing as mp

# задаем период для исходной таблицы tab_0


def func(year, month, day, hour, minutes, tmz, ds):
    conn = sqlite3.connect('db/test_all_moons.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")
    lat = [i for i in range(-90, 91, 10)]
    lon = [i for i in range(-180, 180, 10)]
    tmp = []
    for i in lat:
        for j in lon:
            tmp.append(round(gp(year, month, day,
                                hour, minutes, tmz, i, j)[1], 2))
    dz = tuple(tmp + [ds])

    cur.execute(
        f"insert into tab_0 values {dz}")

    conn.commit()
    cur.close()


start_time = perf_counter()

if __name__ == '__main__':
    date_start = date(year=1930, month=1, day=1)
    date_end = date(year=1930, month=1, day=1)

    try:
        # conn = sqlite3.connect('db/test_all_moons.db')
        # cur = conn.cursor()
        # print("База данных успешно подключена к SQLite")

        while date_start <= date_end:
            p1 = Process(target=func, args=(date_start.year, date_start.month, date_start.day,
                                            hour, minutes, tmz, str(date_start)))

            p1.start()

            p1.join()

            print(date_start)  # видеть лог
            date_start += timedelta(days=1)

        # cur.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)

    # finally:
    #     if (conn):
    #         conn.close()
    #         print("Соединение с SQLite закрыто")

    print(f'{(perf_counter() - start_time)}')
