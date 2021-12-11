import sqlite3
from defs import calc_moon as func
from datetime import date, timedelta
from const import *

real_data = date(year_natal, month_natal, day_natal)
real_data_next = real_data + timedelta(days=1)


def recalc(hour_natal):  # поправка на реальное время для луны
    cur.execute(
        f"select moon from tab_0 where date = '{real_data}'")
    moon_point_1 = cur.fetchone()[0]
    cur.execute(
        f"select moon from tab_0 where date = '{real_data_next}'")
    moon_point_2 = cur.fetchone()[0]

    if moon_point_2 < moon_point_1:
        moon_point = (moon_point_2+360-moon_point_1)/24*hour_natal
    else:
        moon_point = (moon_point_2-moon_point_1)/24*hour_natal
    return moon_point


try:
    conn = sqlite3.connect('db/ephem.db')
    cur = conn.cursor()
    print("База данных создана и успешно подключена к SQLite")

    # находим самую близкую луну из готовых ячеек
    moon_fix = func.calc(lat_natal, lon_natal)
    moon_actual = f'moon_{moon_fix[0]}_{moon_fix[1]}'
    # print(moon_fix, moon_fix[0], moon_fix[1], moon_actual)

    cur.execute(
        f"update tab_0 set moon = {moon_actual} + {recalc(hour_natal)}")
    cur.execute(
        f"update tab_0 set moon = moon - 360 where moon > 360")
    cur.execute(
        f"update tab_0 set moon = round(moon, 1)")

    # предварительная очистка клиентской таблицы
    cur.execute("delete from tab_1")
    # заполняем клиентскую таблицу tab_1 от даты рождения
    cur.execute(
        f"insert into tab_1(date, sun, moon, mercury, venus, mars, jupiter, saturn, uranus, neptune, pluto) select date, sun, moon, mercury, venus, mars, jupiter, saturn, uranus, neptune, pluto from tab_0 where date >= '{real_data}' ")
    print("Клиентская База данных создана")

    conn.commit()
    cur.execute("vacuum")
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")
