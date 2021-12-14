from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
import sqlite3
from const import *
from time import perf_counter
from multiprocessing import Pool, Process, Lock
import multiprocessing as mp

# задаем период для исходной таблицы tab_0


def func(year, month, day, hour, minutes, tmz, ds):
    conn = sqlite3.connect('db/test_mp.db')
    cur = conn.cursor()

    lat = [i for i in range(-90, 91, 30)]
    lon = [i for i in range(-180, 180, 30)]
    tmp = []
    for i in lat:
        for j in lon:
            tmp.append(round(gp(year, month, day,
                                0, 0, 0, i, j)[1], 2))
    dz = tuple(tmp + [str(ds)])

    cur.execute(
        f"insert into tab_0 values {dz}")

    conn.commit()
    cur.close()


start_time = perf_counter()

if __name__ == '__main__':

    conn = sqlite3.connect('db/test_mp.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")
    # очистка таблиц
    cur.execute(''' drop table if exists tab_0 ''')

    def change(lat, lon):
        if lat < 0:
            lat = str(abs(lat)) + 'm'
        if lon < 0:
            lon = str(abs(lon)) + 'm'
        return tmp.append(f'moon_{lat}_{lon}')

    lat = [i for i in range(-90, 91, 30)]
    lon = [i for i in range(-180, 180, 30)]
    tmp = []
    for i in lat:
        for j in lon:
            change(i, j)
    dz = tuple(tmp)

    cur.execute(f'create table tab_0 {dz}')
    cur.execute('alter table tab_0 add column data text')
    conn.commit()
    cur.close()

    date_start = date(year=1930, month=1, day=1)
    date_end = date(year=1930, month=1, day=1)

    while date_start <= date_end:
        p1 = Process(target=func, args=(date_start.year, date_start.month, date_start.day,
                                        hour, minutes, 0, str(date_start)))
        p2 = Process(target=func, args=(date_start.year, date_start.month, date_start.day,
                                        hour, minutes, 0, str(date_start)))
        p3 = Process(target=func, args=(date_start.year, date_start.month, date_start.day,
                                        hour, minutes, 0, str(date_start)))
        p4 = Process(target=func, args=(date_start.year, date_start.month, date_start.day,
                                        hour, minutes, 0, str(date_start)))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()

        print(date_start)  # видеть лог
        date_start += timedelta(days=1)

    print(f'{(perf_counter() - start_time)}')

    # except sqlite3.Error as error:
    #     print("Ошибка при подключении к sqlite", error)

    # finally:
    #     if (conn):
    #         conn.close()
    #         print("Соединение с SQLite закрыто")
