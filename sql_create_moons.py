from time import perf_counter
from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
import sqlite3
from const import *
# создаем отдельный файл для выбранных координат луны

real_data = f'{year_natal}-{month_natal}-{day_natal}'

tm = 'moon_-0_120'
start_time = perf_counter()

try:
    conn = sqlite3.connect(f'db/ephem_{tm}.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

# очистка таблиц
    cur.execute(''' drop table if exists tab ''')
# предварительная очистка клиентской таблицы
    # cur.execute("delete from tab_2")

    create_tab = ''' create table tab (
        data text,
        moon real
    );
    '''

    cur.execute(create_tab)

# скопировать из базы всех лун
    # cur.execute("attach database 'db/ephem_allmoons.db' as ads")
    # cur.execute(
    #     f"insert into tab(data, moon) select data, {tm} from ads.tab_0")

    conn.commit()
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")

print(f'{(perf_counter() - start_time)}')
