import sqlite3

lat = [i for i in range(-90, 91, 10)]
lon = [i for i in range(-180, 180, 10)]
tmp = []
for i in lat:
    for j in lon:
        tmp.append(f'{i}_{j}')

dz = tuple(tmp)

try:
    conn = sqlite3.connect(f'db/ephem_allmoons.db')
    cur = conn.cursor()
    print("База данных подключена к SQLite")

    # очистка таблиц
    cur.execute(''' drop table if exists tab_0 ''')
    print("Предварительная очистка")

    cur.execute(f'create table tab_0 {dz}')
    cur.execute('alter table tab_0 add column data text')

    print("Новая таблица создана")

    conn.commit()
    cur.execute("vacuum")
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")
