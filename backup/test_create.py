import sqlite3

try:
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    print("База данных создана и успешно подключена к SQLite")

    create_tab_0 = ''' create table tab_0 (
        date text primary key,
        moon real not null,
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
    create_tab_1 = ''' create table tab_1 (
        date text primary key,
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

    conn.commit()
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")
