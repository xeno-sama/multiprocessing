from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
import sqlite3
from const import *

start = datetime.now()

try:
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

# задаем период для исходной таблицы tab_0
    date_start = date(year=1930, month=1, day=1)
    date_end = date(year=2050, month=1, day=1)

    while date_start <= date_end:
        _natal = gp(date_start.year, date_start.month, date_start.day,
                    hour, minutes, tmz, lat, lon)
        sun = round(_natal[0], 1)
        moon = round(_natal[1], 1)
        mercury = round(_natal[2], 1)
        venus = round(_natal[3], 1)
        mars = round(_natal[4], 1)
        jupiter = round(_natal[5], 1)
        saturn = round(_natal[6], 1)
        uranus = round(_natal[7], 1)
        neptune = round(_natal[8], 1)
        pluto = round(_natal[9], 1)

# оптимальный шаг 30 по широте и 60 по долготе - погрешность луны в пределах 0.1
        moon_0_0 = round(gp(date_start.year, date_start.month, date_start.day,
                            hour, minutes, tmz, 0.0, 0.0)[1], 1)
        moon_0_60 = round(gp(date_start.year, date_start.month, date_start.day,
                             hour, minutes, tmz, 0.0, 60.0)[1], 1)
        moon_0_120 = round(gp(date_start.year, date_start.month, date_start.day,
                              hour, minutes, tmz, 0.0, 120.0)[1], 1)
        moon_0_180 = round(gp(date_start.year, date_start.month, date_start.day,
                              hour, minutes, tmz, 0.0, 180.0)[1], 1)
        moon_0_120m = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, 0.0, -120.0)[1], 1)
        moon_0_60m = round(gp(date_start.year, date_start.month, date_start.day,
                              hour, minutes, tmz, 0.0, -60.0)[1], 1)

        moon_30_0 = round(gp(date_start.year, date_start.month, date_start.day,
                             hour, minutes, tmz, 30.0, 0.0)[1], 1)
        moon_30_60 = round(gp(date_start.year, date_start.month, date_start.day,
                              hour, minutes, tmz, 30.0, 60.0)[1], 1)
        moon_30_120 = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, 30.0, 120.0)[1], 1)
        moon_30_180 = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, 30.0, 180.0)[1], 1)
        moon_30_120m = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, 30.0, -120.0)[1], 1)
        moon_30_60m = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, 30.0, -60.0)[1], 1)

        moon_60_0 = round(gp(date_start.year, date_start.month, date_start.day,
                             hour, minutes, tmz, 60.0, 0.0)[1], 1)
        moon_60_60 = round(gp(date_start.year, date_start.month, date_start.day,
                              hour, minutes, tmz, 60.0, 60.0)[1], 1)
        moon_60_120 = round(gp(date_start.year, date_start.month, date_start.day,
                            hour, minutes, tmz, 60.0, 120.0)[1], 1)
        moon_60_180 = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, 60.0, 180.0)[1], 1)
        moon_60_120m = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, 60.0, -120.0)[1], 1)
        moon_60_60m = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, 60.0, -60.0)[1], 1)

        moon_90_0 = round(gp(date_start.year, date_start.month, date_start.day,
                             hour, minutes, tmz, 90.0, 0.0)[1], 1)
        moon_90_60 = round(gp(date_start.year, date_start.month, date_start.day,
                              hour, minutes, tmz, 90.0, 60.0)[1], 1)
        moon_90_120 = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, 90.0, 120.0)[1], 1)
        moon_90_180 = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, 90.0, 180.0)[1], 1)
        moon_90_120m = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, 90.0, -120.0)[1], 1)
        moon_90_60m = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, 90.0, -60.0)[1], 1)

        moon_30m_0 = round(gp(date_start.year, date_start.month, date_start.day,
                              hour, minutes, tmz, -30.0, 0.0)[1], 1)
        moon_30m_60 = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, -30.0, 60.0)[1], 1)
        moon_30m_120 = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, -30.0, 120.0)[1], 1)
        moon_30m_180 = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, -30.0, 180.0)[1], 1)
        moon_30m_120m = round(gp(date_start.year, date_start.month, date_start.day,
                                 hour, minutes, tmz, -30.0, -120.0)[1], 1)
        moon_30m_60m = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, -30.0, -60.0)[1], 1)

        moon_60m_0 = round(gp(date_start.year, date_start.month, date_start.day,
                              hour, minutes, tmz, -60.0, 0.0)[1], 1)
        moon_60m_60 = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, -60.0, 60.0)[1], 1)
        moon_60m_120 = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, -60.0, 120.0)[1], 1)
        moon_60m_180 = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, -60.0, 180.0)[1], 1)
        moon_60m_120m = round(gp(date_start.year, date_start.month, date_start.day,
                                 hour, minutes, tmz, -60.0, -120.0)[1], 1)
        moon_60m_60m = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, -60.0, -60.0)[1], 1)

        moon_90m_0 = round(gp(date_start.year, date_start.month, date_start.day,
                              hour, minutes, tmz, -90.0, 0.0)[1], 1)
        moon_90m_60 = round(gp(date_start.year, date_start.month, date_start.day,
                               hour, minutes, tmz, -90.0, 60.0)[1], 1)
        moon_90m_120 = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, -90.0, 120.0)[1], 1)
        moon_90m_180 = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, -90.0, 180.0)[1], 1)
        moon_90m_120m = round(gp(date_start.year, date_start.month, date_start.day,
                                 hour, minutes, tmz, -90.0, -120.0)[1], 1)
        moon_90m_60m = round(gp(date_start.year, date_start.month, date_start.day,
                                hour, minutes, tmz, -90.0, -60.0)[1], 1)

        data = str(date_start)
        cur.execute("insert into tab_0 values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (data, sun, moon, mercury, venus, mars, jupiter, saturn, uranus, neptune, pluto, moon_0_0, moon_0_60, moon_0_120, moon_0_180, moon_0_120m, moon_0_60m, moon_30_0, moon_30_60, moon_30_120, moon_30_180, moon_30_120m, moon_30_60m, moon_60_0, moon_60_60, moon_60_120, moon_60_180, moon_60_120m, moon_60_60m, moon_90_0, moon_90_60, moon_90_120, moon_90_180, moon_90_120m, moon_90_60m, moon_30m_0, moon_30m_60, moon_30m_120, moon_30m_180, moon_30m_120m, moon_30m_60m, moon_60m_0, moon_60m_60, moon_60m_120, moon_60m_180, moon_60m_120m, moon_60m_60m, moon_90m_0, moon_90m_60, moon_90m_120, moon_90m_180, moon_90m_120m, moon_90m_60m))
        date_start += timedelta(days=1)

        print(date_start)  # видеть лог

    conn.commit()
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")

end = datetime.now()
print(end-start)
