import sqlite3
from datetime import date, timedelta
# код будет копировать в ephem.db moon из db/moons


def find_moon(year, month, day, hour, minutes, _lat, _lon):
    # поиск файла базы лун по заданным координатам

    lat = round(_lat/10)*10
    lon = round(_lon/10)*10
    natal_date = str(date(year, month, day))
    next_date = str(date(year, month, day) + timedelta(days=1))
    _time_coef = (hour + minutes/0.6)/0.24

    if lat < 0:
        lat = str(abs(lat)) + 'm'
    if lon < 0:
        lon = str(abs(lon)) + 'm'

    db_name = f'db/moons/moon_{lat}_{lon}.db'

    try:
        conn = sqlite3.connect('db/ephem.db')
        cur = conn.cursor()
        print("База данных успешно подключена к SQLite")

    # предварительная очистка клиентской таблицы
        cur.execute("delete from tab_1")
        cur.execute("delete from tab_final")

    # скопировать из другой базы
        cur.execute(f"attach database '{db_name}' as ads")
        cur.execute(
            "insert into tab_1(data, moon) select data, moon from ads.tab_0")

    # скопировать из базовой таблицы tab_0 в клиентскую tab_final
        cur.execute(
            f"insert into tab_final select data,sun,moon,mercury,venus,mars,jupiter,saturn,uranus,neptune,pluto from tab_0")

    # перенести нужное значение из таблицы tab_1 в главную таблицу tab_0
        cur.execute(
            "update tab_final set moon = tab_1.moon from tab_1 where tab_final.data = tab_1.data")

        conn.commit()
        cur.execute("vacuum")
        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)

    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


year = 1977
month = 5
day = 27
hour = 16
minutes = 52
lat = 72.6
lon = 14.9

find_moon(year, month, day, hour, minutes, lat, lon)
