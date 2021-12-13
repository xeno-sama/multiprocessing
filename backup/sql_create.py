import sqlite3
from defs.gradusPlanets import calc as gp
from datetime import date, timedelta
from time import perf_counter

try:
    conn = sqlite3.connect('db/ephem.db')
    cur = conn.cursor()
    print("База данных подключена к SQLite")

    # очистка таблиц
    cur.execute(''' drop table if exists tab_0 ''')
    cur.execute(''' drop table if exists tab_final ''')
    # print("Предварительная очистка")

    create_tab_0 = ''' create table if not exists tab_0  (
        data text not null,
        sun real not null,
        moon real not null,
        mercury real not null,
        venus real not null,
        mars real not null,
        jupiter real not null,
        saturn real not null,
        uranus real not null,
        neptune real not null,
        pluto real not null,
        step_mercury real not null,
        step_venus real not null,
        step_mars real not null,
        step_jupiter real not null
    );
    '''

    create_tab_final = ''' create table if not exists tab_final  (
        data text,
        sun real,
        moon real,
        mercury real,
        venus real,
        mars real,
        jupiter real,
        saturn real,
        uranus real,
        neptune real,
        pluto real
    );
    '''
    cur.execute(create_tab_0)
    cur.execute(create_tab_final)

# предварительная очистка клиентской таблицы или если надо частями заполнять таблицу
# только меняем даты выборки
    cur.execute("delete from tab_0")
    cur.execute("delete from tab_final")

    date_start = date(year=1900, month=1, day=1)
    date_end = date(year=1900, month=2, day=1)

    def calc_velo(_natal, _natal_next):
        # расчет смещения планеты за день / учитываем ☿ ♀ ♂ ♃
        _tmp = []
        for i in range(2, 6, 1):
            if _natal_next[i] - _natal[i] < 0 and abs(_natal_next[i] - _natal[i]) > 350:
                _tmp.append(round((_natal_next[i] - _natal[i] + 360), 3))
            elif _natal_next[i] - _natal[i] < 0 and abs(_natal_next[i] - _natal[i]) < 350:
                _tmp.append(round((_natal_next[i] - _natal[i]), 3))
            else:
                _tmp.append(round((_natal_next[i] - _natal[i]), 3))
        return _tmp

    while date_start <= date_end:
        date_next = date_start + timedelta(days=1)
        _natal_next = [round(i, 3) for i in gp(date_next.year, date_next.month, date_next.day,
                                               0, 0, 0, 0.0, 0.0)]
        _natal = [round(i, 3) for i in gp(date_start.year, date_start.month, date_start.day,
                                          0, 0, 0, 0.0, 0.0)]
        _step = calc_velo(_natal, _natal_next)

        dz = tuple([str(date_start)] + _natal + _step)

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
