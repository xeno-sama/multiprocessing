import sqlite3
from datetime import date, timedelta
# код будет копировать в ephem.db moon из db/moons


def find_realpos(planet, step):
    _planet = planet + step
    if _planet > 360:
        _planet = 360 - _planet
    return _planet


def find_moon(year, month, day, hour, minutes, _lat, _lon):
    # поиск файла базы лун по заданным координатам

    lat = round(_lat/10)*10
    lon = round(_lon/10)*10
    natal_date = str(date(year, month, day))
    next_date = str(date(year, month, day) + timedelta(days=1))
    _time_coef = (hour + minutes/60)/0.24/100

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
        cur.execute("delete from tab_final")

    # скопировать из другой базы
        cur.execute(f"attach database '{db_name}' as ads")

    # скопировать из базовой таблицы tab_0 в клиентскую tab_final
        cur.execute(
            f"insert into tab_final select data,sun,moon,mercury,venus,mars,jupiter,saturn,uranus,neptune,pluto from tab_0")

    # перенести нужное значение луны из таблицы tab_1 в клиентскую таблицу tab_final
        cur.execute(
            "update tab_final set moon = tab_0.moon from ads.tab_0 where tab_final.data = ads.tab_0.data")
    ## ##
# исправляем значения планет в соотв с реальным временем ☉ ☽ ☿ ♀ ♂ ♃

        cur.execute(
            f"update tab_final set sun = 1*{_time_coef} + sun")
        cur.execute(
            "update tab_final set sun = case when sun >= 360 then round((sun-360),2) else round(sun,2) end")

        cur.execute(
            f"update tab_final set moon = 13*{_time_coef} + moon")
        cur.execute(
            "update tab_final set moon = case when moon >= 360 then round((moon-360),2) else round(moon,2) end")

        cur.execute(
            f"update tab_final set mercury = (tab_0.step_mercury*{_time_coef} + tab_0.mercury) from tab_0 where tab_final.data = tab_0.data")
        cur.execute(
            "update tab_final set mercury = case when mercury >= 360 then round((mercury-360),2) else round(mercury,2) end")

        cur.execute(
            f"update tab_final set venus = (tab_0.step_venus*{_time_coef} + tab_0.venus) from tab_0 where tab_final.data = tab_0.data")
        cur.execute(
            "update tab_final set venus = case when venus >= 360 then round((venus-360),2) else round(venus,2) end")

        cur.execute(
            f"update tab_final set mars = (tab_0.step_mars*{_time_coef} + tab_0.mars) from tab_0 where tab_final.data = tab_0.data")
        cur.execute(
            "update tab_final set mars = case when mars >= 360 then round((mars-360),2) else round(mars,2) end")

        cur.execute(
            f"update tab_final set jupiter = (tab_0.step_jupiter*{_time_coef} + tab_0.jupiter) from tab_0 where tab_final.data = tab_0.data")
        cur.execute(
            "update tab_final set jupiter = case when jupiter >= 360 then round((jupiter-360),2) else round(jupiter,2) end")

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
