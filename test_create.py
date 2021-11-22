import sqlite3

try:
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    print("База данных создана и успешно подключена к SQLite")

    create_tab_0 = ''' create table tab_0 (
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
        pluto real not null,
        moon_0_0 real not null,
        moon_0_60 real not null,
        moon_0_120 real not null,
        moon_0_180 real not null,
        moon_0_60m real not null,
        moon_0_120m real not null,      
        moon_30_0 real not null,
        moon_30_60 real not null,
        moon_30_120 real not null,
        moon_30_180 real not null,
        moon_30_60m real not null,
        moon_30_120m real not null,
        moon_60_0 real not null,
        moon_60_60 real not null,
        moon_60_120 real not null,
        moon_60_180 real not null,
        moon_60_60m real not null,
        moon_60_120m real not null,
        moon_90_0 real not null,
        moon_90_60 real not null,
        moon_90_120 real not null,
        moon_90_180 real not null,
        moon_90_60m real not null,
        moon_90_120m real not null,  
        moon_30m_0 real not null,
        moon_30m_60 real not null,
        moon_30m_120 real not null,
        moon_30m_180 real not null,
        moon_30m_60m real not null,
        moon_30m_120m real not null,
        moon_60m_0 real not null,
        moon_60m_60 real not null,
        moon_60m_120 real not null,
        moon_60m_180 real not null,
        moon_60m_60m real not null,
        moon_60m_120m real not null,
        moon_90m_0 real not null,
        moon_90m_60 real not null,
        moon_90m_120 real not null,
        moon_90m_180 real not null,
        moon_90m_60m real not null,
        moon_90m_120m real not null
    );
    '''

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

    # uranus = 999
    # sun = 99
    # moon = 111
    # cur.execute("insert into tab1 values (?,?,?)",
    #             (uranus, sun, moon))

    # create_tab2 = ''' create table tab2 (
    #     sun real,
    #     moon real
    # );
    # '''
    # cur.execute(create_tab2)

    # cur.execute("insert into tab2 select sun,moon from tab1")
