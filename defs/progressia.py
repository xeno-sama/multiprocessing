# расчет медленной прогрессии
from datetime import datetime, timedelta


async def calc(year, month, day, hour, minutes, pr_year, pr_month, pr_day, pr_hour, pr_minutes):

    d0 = datetime(year, month, day, hour, minutes)
    d1 = datetime(pr_year, pr_month, pr_day, pr_hour, pr_minutes)
    delta = d1 - d0
    progr = delta.days / 365.25  # 1 день = 1 год
    progr_day = (d0+timedelta(days=progr))  # то что надо для прогрессии

    progr_date = progr_day.strftime("%Y %m %d %H %M")
    year = int(progr_date[0:4])
    month = int(progr_date[5:7])
    day = int(progr_date[8:10])
    hour = int(progr_date[11:13])
    minutes = int(progr_date[14:])

    return year, month, day, hour, minutes
