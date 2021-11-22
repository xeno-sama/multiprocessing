from datetime import date, datetime, timedelta
from defs.gradusPlanets import calc as gp
from const import *
import threading

lock = threading.Lock

start = datetime.now()

tmp = []
date_start = date(year=1977, month=1, day=1)
date_end = date(year=1977, month=1, day=10)


class threadtester (threading.Thread):
    def __init__(self, x, y, z):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y
        self.z = z

    def run(self):
        thread_test(self.x, self.y, self.z)
        # print(self.name)


def thread_test(year, month, day):

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
    print(moon_0_0, moon_0_60, moon_0_120, moon_0_180, moon_0_120m, moon_0_60m)
    lock.acuire()
    lock.release()


while date_start <= date_end:

    thread1 = threadtester(date_start.year, date_start.month, date_start.day)

    thread1.start()

    date_start += timedelta(days=1)

end = datetime.now()
print(end-start)


# start = datetime.now()
# x = []


# while date_start <= date_end:

# for index in range(1, 4):
#     x1 = _thread.start_new_thread(calc, (1977, 5, index,
#                                          12, 0, 6, 0.0, 0.0))
#     x2 = _thread.start_new_thread(calc, (1977, 5, index,
#                                          12, 0, 6, 0.0, 60.0))
#     x3 = _thread.start_new_thread(calc, (1977, 5, index,
#                                          12, 0, 6, 0.0, 120.0))
#     x.append([x1, x2, x3])

# date_start += timedelta(days=1)
# x1 = _thread.start_new_thread(calc, (1977, 5, 27, 12, 0, 6, 42.0, 75.0))

# print(x1)
# end = datetime.now()
# print(end-start)

# def daterange(date_start, date_end):
#     for n in range(int((date_end - date_start).days)):
#         yield date_start + timedelta(n)
