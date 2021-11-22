
from skyfield.api import utc, load
from datetime import datetime, timedelta
from numpy import cos, sin, tan, arccos, arctan, radians, degrees

# Расчет позиций Домов


async def calc(year, month, day, hour, minutes, popravka, _lat, _lon):  # popravka +6 Бишкек

    ts = load.timescale()
    day = datetime(year, month, day, hour, minutes,
                   tzinfo=utc) + timedelta(hours=-popravka)
    t = ts.utc(int(day.strftime("%Y")), int(day.strftime("%m")), int(day.strftime("%d")),
               int(day.strftime("%H")), int(day.strftime("%M")))

    # прямое восхождение, t.gmst - звездное время, ex: 4,97 = Долгота/15 = 74,6/15
    _pv = (t.gmst + _lon / 15) * 15
    pv = radians(_pv)
    lat = radians(_lat)
    e = radians(23.43)  # склонение эклиптики в радианах

    # формула для МС
    mc = degrees(arctan(tan(pv) / cos(e)))
    # формула для AS
    asc = degrees(arctan(cos(pv) / -(tan(lat) * sin(e) + sin(pv) * cos(e))))
    # вспомогательный угол для куспидов
    c = arccos(-tan(e) * sin(pv) * tan(lat))

    ii = degrees(arctan(cos(pv + c / 3) / -
                 (tan(lat) * sin(e) + sin(pv + c / 3) * cos(e))))
    iii = degrees(arctan(cos(pv + 2 * c / 3) / -
                  (tan(lat) * sin(e) + sin(pv + 2 * c / 3) * cos(e))))
    xi = degrees(arctan(cos(pv - 2 * c / 3) / -
                 (tan(lat) * sin(e) + sin(pv - 2 * c / 3) * cos(e))))
    xii = degrees(arctan(cos(pv - c / 3) / -
                  (tan(lat) * sin(e) + sin(pv - c / 3) * cos(e))))

    if mc < 0:
        mc += 180  # МС должен быть в пределах 10гр от Pv и положительным
    if abs(mc - pv) > 10:
        mc += 180
    if mc < 180:
        ic = mc + 180  # IC отстоит на 180гр
    elif mc >= 180:
        ic = mc - 180

    if asc < 0:
        asc += 180
        if asc < mc:
            asc += 180
            if asc > 360:
                asc -= 360
    if 0 < asc < mc:
        asc += 180
        if asc < mc:
            asc += 180
        if asc > 360:
            asc -= 360

    if asc < 180:
        ds = asc + 180  # DS отстоит на 180гр
    elif asc >= 180:
        ds = asc - 180

    while ii < asc:
        ii += 180
    if ii > 360:
        ii = ii - 360
    if ii > 180:
        viii = ii - 180
    else:
        viii = ii + 180

    while iii < ii:
        iii += 180
    if iii > 360:
        iii = iii - 360
    if iii > 180:
        ix = iii - 180
    else:
        ix = iii + 180

    while xi < mc:
        xi += 180
    if xi > 360:
        xi = xi - 360
    if xi > 180:
        v = xi - 180
    else:
        v = xi + 180

    while xii < xi:
        xii += 180
    if xii > 360:
        xii = xii - 360
    if xii > 180:
        vi = xii - 180
    else:
        vi = xii + 180

    return asc, ii, iii, ic, v, vi, ds, viii, ix, mc, xi, xii
