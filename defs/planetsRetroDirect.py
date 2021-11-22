# расчет направления и скорости планет, ретро, смещение = 1час
from defs.gradusPlanets import calc as gp


async def calc1(year, month, day, hour, minutes, tmz, lat, lon, _natal):
    def bin(x, y):
        if x - y < 0:
            return -1
        else:
            return 1

    velo = []

    if hour < 23:
        hour_v = hour + 1
        temp_v = await gp(year, month, day, hour_v, minutes, tmz, lat, lon)
    else:
        hour_v = hour - 1
        temp_v = await gp(year, month, day, hour_v, minutes, tmz, lat, lon)

    for x in range(10):
        velo.append(bin(temp_v[x], _natal[x]))

    return velo


# вариант для pandas
# def calc_pd(year, month, day, hour, minutes, popravka, lat, lon, gp):
#     def bin(x, y):
#         if x - y < 0:
#             return -1
#         else:
#             return 1

#     velo = []
#     if hour < 23:
#         hour_v = hour + 1
#         temp_v = gp(year, month, day, hour_v, minutes, 0, lat, lon)
#         for x in range(10):
#             velo.append(bin(temp_v[x], gp[x]))
#     else:
#         hour_v = hour - 1
#         temp_v = gp(year, month, day, hour_v, minutes, 0, lon, lat)
#         for x in range(10):
#             velo.append(bin(gp[x], temp_v[x]))

#     return velo
