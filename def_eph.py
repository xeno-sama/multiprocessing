from const import *
from datetime import date, timedelta
from defs.gradusPlanets import calc as gp
import math

date_start = date(year=1977, month=1, day=1)
date_end = date(year=1977, month=1, day=10)


def test(dayx):
    sum = 0
    start_date = date(2021, 1, 1)
    end_date = date(2021, 1, 3)
    delta = timedelta(days=1)

    while start_date <= end_date:
        sum += 1000000000000**(dayx*200)

        start_date += delta

    # moon_0_0 = round(gp(date_start.year, date_start.month, dayx,
    #                     hour, minutes, tmz, 0.0, 0.0)[1], 1)
    # moon_0_60 = round(gp(date_start.year, date_start.month, dayx,
    #                      hour, minutes, tmz, 0.0, 60.0)[1], 1)
    # moon_0_120 = round(gp(date_start.year, date_start.month, dayx,
    #                       hour, minutes, tmz, 0.0, 120.0)[1], 1)
    # moon_0_180 = round(gp(date_start.year, date_start.month, dayx,
    #                       hour, minutes, tmz, 0.0, 180.0)[1], 1)
    # moon_0_120m = round(gp(date_start.year, date_start.month, dayx,
    #                        hour, minutes, tmz, 0.0, -120.0)[1], 1)
    # moon_0_60m = round(gp(date_start.year, date_start.month, dayx,
    #                       hour, minutes, tmz, 0.0, -60.0)[1], 1)

    return sum
    # , moon_0_60, moon_0_120, moon_0_180, moon_0_120m, moon_0_60m
