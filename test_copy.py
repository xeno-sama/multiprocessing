import sqlite3
from defs import calc_moon as func
from const import *
real_data = f'{year_natal}-{month_natal}-{day_natal}'

try:
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    print("База данных создана и успешно подключена к SQLite")

    # находим самую близкую луну
    moon_fix = func.calc(lat_natal, lon_natal)
    moon_actual = f'moon_{moon_fix[0]}_{moon_fix[1]}'
    cur.execute(f"update tab_0 set moon = {moon_actual} ")

    # предварительная очистка клиентской таблицы
    cur.execute("delete from tab_1")
    # заполняем клиентскую таблицу tab_1 от даты рождения
    cur.execute(
        f"insert into tab_1(date, sun, moon, mercury, venus, mars, jupiter, saturn, uranus, neptune, pluto) select date, sun, moon, mercury, venus, mars, jupiter, saturn, uranus, neptune, pluto from tab_0 where date >= '{real_data}' ")

    conn.commit()
    cur.execute("vacuum")
    # conn.commit()
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")
