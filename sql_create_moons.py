from time import perf_counter
from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
import sqlite3
from const import *

real_data = f'{year_natal}-{month_natal}-{day_natal}'

tm = '0_120'
start_time = perf_counter()

try:
    conn = sqlite3.connect(f'test_check_{tm}.db')
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

# скопировать из главной базы
    cur.execute("attach database 'test_check.db' as ads")
    cur.execute(
        f"insert into tab(data, moon) select data, moon_{tm} from ads.tab_0")

    conn.commit()
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")

print(f'{(perf_counter() - start_time)}')
