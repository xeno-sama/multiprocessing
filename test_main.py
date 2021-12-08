from defs.gradusPlanets import calc as gp
from datetime import date, datetime, timedelta
import sqlite3
from const import *

real_data = f'{year_natal}-{month_natal}-{day_natal}'
start = datetime.now()

try:
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    print("База данных успешно подключена к SQLite")

    # cur.execute("delete from tab_0")
    # cur.execute("delete from tab_1")

    conn.commit()
    cur.execute("vacuum")
    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if (conn):
        conn.close()
        print("Соединение с SQLite закрыто")

end = datetime.now()
print(end-start)

# tmp = []
#    for row in cur.execute(
#             "select date from ephemerides where venus - moon > 250 and moon < 50 and date between '2027-01-30' and '2029-12-30'"):
#         tmp.append(row[0])
#     print(tmp)


###########################################

# переписать таблицу с уточнением по луне
# cur.execute("update ephemerides set moon = moon + 10 where moon > 0 ")

# скопировать в другую базу
# cur.execute("attach database 'ephem03.db' as other")
# cur.execute("insert into other.ephemerides select * from ephemerides")

# урезать полную таблицу в краткую, начиная с даты рождения
# cur.execute("delete from ephemerides where date > '2020-02-01' ")

# сжатие базы
# cur.execute("vacuum")

# найти нужнул луну и скопировать ее в начальную moon_0_0 переделать в moon
# lst = func.calc(42, -75)
# df = f'moon_{lst[0]}_{lst[1]}'
# cur.execute(f"update ephemerides set moon_0_0 = {df} ")

###########################################


# date_start = date(year=2018, month=1, day=1)
# date_end = date(year=2019, month=1, day=1)

# date_start2 = date(year=2018, month=1, day=1)
# date_end2 = date(year=2019, month=1, day=1)

# while date_start <= date_end:
#     _natal = gp(date_start.year, date_start.month, date_start.day,
#                 hour, minutes, tmz, lat, lon)
#     moon = round(_natal[1], 1)
#     tmp1.append(moon)
#     date_start += timedelta(days=60)

# while date_start2 <= date_end2:
#     _natal = gp(date_start2.year, date_start2.month, date_start2.day,
#                 hour, minutes, tmz, 0.0, 0.0)
#     moon2 = round(_natal[1], 1)
#     tmp2.append(moon2)
#     date_start2 += timedelta(days=30)

# for i in range(len(tmp2)-1):
#     tmp.append(round(tmp1[i]-tmp2[i], 2))

# print(tmp)

# i = 0
# date_start = date(year=2020, month=1, day=1)
# date_end = date(year=2020, month=1, day=5)

# cur.execute("attach database 'ephem_moon_copy.db' as other")

# while date_start <= date_end:
#     moon_0_120 = tmp[i]
#     cur.execute("insert into other.ephemerides values (?)",
#                 (moon_0_120))
#     date_start += timedelta(days=1)
#     i += 1
