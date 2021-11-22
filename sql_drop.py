import sqlite3


try:
    conn = sqlite3.connect('ephem02.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

    cur.execute("delete from ephemerides")
    conn.commit()
    print("База данных очищена")

    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")
