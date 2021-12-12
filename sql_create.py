import sqlite3
from defs.gradusPlanets import calc as gp
from datetime import date, timedelta
from time import perf_counter

try:
    conn = sqlite3.connect('db/ephem.db')
    cur = conn.cursor()
    print("База данных подключена к SQLite")

    # очистка таблиц
    # cur.execute(''' drop table if exists tab_0 ''')
    # cur.execute(''' drop table if exists tab_1 ''')
    # cur.execute(''' drop table if exists tab_final ''')
    # print("Предварительная очистка")

    create_tab_0 = ''' create table if not exists tab_0  (
        data text primary key,
        sun real not null,
        moon real not null,
        mercury real not null,
        venus real not null,
        mars real not null,
        jupiter real not null,
        saturn real not null,
        uranus real not null,
        neptune real not null,
        pluto real not null
    );
    '''
# вторая таблица tab_1 для клиента - собирается из первой tab_0 + реальное время рождения
    create_tab_1 = ''' create table if not exists tab_1 (
        data text not null,
        moon real not null
    );
    '''
    create_tab_final = ''' create table if not exists tab_final  (
        data text primary key,
        sun real not null,
        moon real not null,
        mercury real not null,
        venus real not null,
        mars real not null,
        jupiter real not null,
        saturn real not null,
        uranus real not null,
        neptune real not null,
        pluto real not null
    );
    '''
    cur.execute(create_tab_0)
    cur.execute(create_tab_1)
    cur.execute(create_tab_final)

# предварительная очистка клиентской таблицы или если надо частями заполнять таблицу
# только меняем даты выборки
    cur.execute("delete from tab_0")
    cur.execute("delete from tab_1")
    cur.execute("delete from tab_final")

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
    cur.execute("vacuum")
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")
