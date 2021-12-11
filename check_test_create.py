import sqlite3

try:
    conn = sqlite3.connect('test_check.db')
    cur = conn.cursor()
    print("База данных подключена к SQLite")

    # очистка таблиц
    cur.execute(''' drop table if exists tab_0 ''')
    cur.execute(''' drop table if exists tab_1 ''')
    print("Предварительная очистка")

# создать таблицу со всеми планетами (moon_0_60 для тестов)
    create_tab_0 = ''' create table tab_0 (
        data text,
        moon real,
        moon_0_60 real,
        moon_0_90 real,
        moon_0_120 real
    );
    '''

# эта таблица нужна -> вставить в нее луну и дату из главной таблицы всех лун
# и после проапдейтить значение луны в первую таблицу tab_0
    create_tab_1 = ''' create table tab_1 (
        data text,
        moon real
    );
    '''

    cur.execute(create_tab_0)
    cur.execute(create_tab_1)
    print("Новая таблица создана")
    conn.commit()
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")

        # data text primary key,
        # moon_0_0 real not null,
        # moon_30_0 real not null,
        # moon_30_60 real not null,
        # moon_30_120 real not null,
        # moon_30_180 real not null,
        # moon_30_60m real not null,
        # moon_30_120m real not null,
        # moon_60_0 real not null,
        # moon_60_60 real not null,
        # moon_60_120 real not null,
        # moon_60_180 real not null,
        # moon_60_60m real not null,
        # moon_60_120m real not null,
        # moon_90_0 real not null,
        # moon_90_60 real not null,
        # moon_90_120 real not null,
        # moon_90_180 real not null,
        # moon_90_60m real not null,
        # moon_90_120m real not null,
        # moon_30m_0 real not null,
        # moon_30m_60 real not null,
        # moon_30m_120 real not null,
        # moon_30m_180 real not null,
        # moon_30m_60m real not null,
        # moon_30m_120m real not null,
        # moon_60m_0 real not null,
        # moon_60m_60 real not null,
        # moon_60m_120 real not null,
        # moon_60m_180 real not null,
        # moon_60m_60m real not null,
        # moon_60m_120m real not null,
        # moon_90m_0 real not null,
        # moon_90m_60 real not null,
        # moon_90m_120 real not null,
        # moon_90m_180 real not null,
        # moon_90m_60m real not null,
        # moon_90m_120m real not null


# moon_0_120 real not null,
# moon_0_150 real not null,
# moon_0_180 real not null,
# moon_0_30m real not null,
# moon_0_60m real not null,
# moon_0_90m real not null,
# moon_0_120m real not null,
# moon_0_150m real not null,
# moon_0_180m real not null
