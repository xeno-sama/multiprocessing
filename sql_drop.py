import sqlite3

try:
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

    # cur.execute("delete from tab_0")
    # cur.execute("delete from tab_1")
    conn.commit()
    print("База данных очищена")

    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")
