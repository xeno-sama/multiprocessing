from re import findall   # регулярное выражение
from skyfield import api
# Topos(lat, lon) float  Топоцентрика
from skyfield.api import utc, wgs84  # iers2010 альтернатива wsg84#
from datetime import datetime, timedelta


def calc(year, month, day, hour, minutes, tmz, lat, lon):

    ts = api.load.timescale()
    # обяз. функции old de421

    na = api.load('de421.bsp')
    day = datetime(year, month, day, hour, minutes,
                   tzinfo=utc) + timedelta(hours=-tmz)
    # по гринвичу UTC=0
    t = ts.utc(day)

    earth = na['earth']  # точка отсчета с земли
    topos = wgs84.latlon(lat, lon)
    mytown = earth + topos

    pos_sun = mytown.at(t).observe(na['sun'])
    pos_moon = mytown.at(t).observe(na['moon'])
    pos_mercury = mytown.at(t).observe(na['mercury barycenter'])
    pos_venus = mytown.at(t).observe(na['venus barycenter'])
    pos_mars = mytown.at(t).observe(na['mars barycenter'])
    pos_jupiter = mytown.at(t).observe(na['jupiter barycenter'])
    pos_saturn = mytown.at(t).observe(na['saturn barycenter'])
    pos_uranus = mytown.at(t).observe(na['uranus barycenter'])
    pos_neptune = mytown.at(t).observe(na['neptune barycenter'])
    pos_pluto = mytown.at(t).observe(na['pluto barycenter'])

    # lon_planet - градус планеты

    lat_sun, lon_sun, d_sun = pos_sun.apparent().ecliptic_latlon(epoch='date')
    lat_moon, lon_moon, d_moon = pos_moon.apparent().ecliptic_latlon(epoch='date')
    lat_mercury, lon_mercury, d_mercury = pos_mercury.apparent().ecliptic_latlon(epoch='date')
    lat_venus, lon_venus, d_venus = pos_venus.apparent().ecliptic_latlon(epoch='date')
    lat_mars, lon_mars, d_mars = pos_mars.apparent().ecliptic_latlon(epoch='date')
    lat_jupiter, lon_jupiter, d_jupiter = pos_jupiter.apparent().ecliptic_latlon(epoch='date')
    lat_saturn, lon_saturn, d_saturn = pos_saturn.apparent().ecliptic_latlon(epoch='date')
    lat_uranus, lon_uranus, d_uranus = pos_uranus.apparent().ecliptic_latlon(epoch='date')
    lat_neptune, lon_neptune, d_neptune = pos_neptune.apparent().ecliptic_latlon(epoch='date')
    lat_pluto, lon_pluto, d_pluto = pos_pluto.apparent().ecliptic_latlon(epoch='date')

    # преобразование из строки - нужных координат

    tmp = [lon_sun, lon_moon, lon_mercury, lon_venus, lon_mars,
           lon_jupiter, lon_saturn, lon_uranus, lon_neptune, lon_pluto]

    planetes = []

    for i in range(len(tmp)):
        nums = findall(r'\d*\.\d+|\d+', str(tmp[i]))
        nums = [float(i) for i in nums]
        planetes.append(nums[0] + nums[1]/60 + nums[2]/6000)
    return planetes


def calc_pd(dat, lat, lon):

    ts = api.load.timescale()
    na = api.load('de421.bsp')
    t = ts.utc(dat)
    earth = na['earth']  # точка отсчета с земли
    topos = wgs84.latlon(lat, lon)
    mytown = earth + topos

    pos_sun = mytown.at(t).observe(na['sun'])
    pos_moon = mytown.at(t).observe(na['moon'])
    pos_mercury = mytown.at(t).observe(na['mercury barycenter'])
    pos_venus = mytown.at(t).observe(na['venus barycenter'])
    pos_mars = mytown.at(t).observe(na['mars barycenter'])
    pos_jupiter = mytown.at(t).observe(na['jupiter barycenter'])
    pos_saturn = mytown.at(t).observe(na['saturn barycenter'])
    pos_uranus = mytown.at(t).observe(na['uranus barycenter'])
    pos_neptune = mytown.at(t).observe(na['neptune barycenter'])
    pos_pluto = mytown.at(t).observe(na['pluto barycenter'])

    # lon_planet - градус планеты

    lat_sun, lon_sun, d_sun = pos_sun.apparent().ecliptic_latlon(epoch='date')
    lat_moon, lon_moon, d_moon = pos_moon.apparent().ecliptic_latlon(epoch='date')
    lat_mercury, lon_mercury, d_mercury = pos_mercury.apparent().ecliptic_latlon(epoch='date')
    lat_venus, lon_venus, d_venus = pos_venus.apparent().ecliptic_latlon(epoch='date')
    lat_mars, lon_mars, d_mars = pos_mars.apparent().ecliptic_latlon(epoch='date')
    lat_jupiter, lon_jupiter, d_jupiter = pos_jupiter.apparent().ecliptic_latlon(epoch='date')
    lat_saturn, lon_saturn, d_saturn = pos_saturn.apparent().ecliptic_latlon(epoch='date')
    lat_uranus, lon_uranus, d_uranus = pos_uranus.apparent().ecliptic_latlon(epoch='date')
    lat_neptune, lon_neptune, d_neptune = pos_neptune.apparent().ecliptic_latlon(epoch='date')
    lat_pluto, lon_pluto, d_pluto = pos_pluto.apparent().ecliptic_latlon(epoch='date')

    # преобразование из строки - нужных координат

    tmp = [lon_sun, lon_moon, lon_mercury, lon_venus, lon_mars,
           lon_jupiter, lon_saturn, lon_uranus, lon_neptune, lon_pluto]

    planets = []

    for i in range(len(tmp)):
        nums = findall(r'\d*\.\d+|\d+', str(tmp[i]))
        nums = [float(i) for i in nums]
        planets.append(nums[0] + nums[1]/60 + nums[2]/6000)
    return planets

    # print(calc(1977, 5, 27, 16, 52, 6, 42, 75))
