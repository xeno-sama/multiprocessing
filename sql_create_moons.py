from defs.gradusPlanets import calc as gp
import sqlite3
# создаем отдельный файл для выбранных координат луны

conn = sqlite3.connect('db/ephem_allmoons.db')
cur = conn.cursor()
print("База данных успешно подключена к SQLite")

cur.execute("select name from PRAGMA_TABLE_INFO('tab_0')")
list_colnames = [i[0] for i in cur.fetchall()][:-1]

cur.close()


def create_moons(moon_coord):
    try:
        conn = sqlite3.connect(f'db/moons/{moon_coord}.db')
        cur = conn.cursor()
        print("База данных успешно создана/подключена к SQLite")

    # очистка таблиц
        cur.execute(''' drop table if exists tab_0 ''')

        create_tab = ''' create table if not exists tab_0 (
            data text,
            moon real
        );
        '''
        cur.execute(create_tab)

    # скопировать из базы всех лун
        cur.execute("attach database 'db/ephem_allmoons.db' as ads")
        cur.execute(
            f"insert into tab_0(data, moon) select data, {moon_coord} from ads.tab_0")

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)

    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


for i in list_colnames:
    create_moons(f'{i}')
