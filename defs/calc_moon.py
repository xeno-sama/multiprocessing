def calc(x, y):

    lon_0_60 = [x for x in range(0, 60)]
    lon_60_120 = [x for x in range(60, 120)]
    lon_120_180 = [x for x in range(120, 180)]

    lon_180_120_m = [x for x in range(-180, -120)]
    lon_120_60_m = [x for x in range(-120, -60)]
    lon_60_0_m = [x for x in range(-60, 0)]

    list_lon = (lon_0_60, lon_60_120, lon_120_180,
                lon_180_120_m, lon_120_60_m, lon_60_0_m)

    lat_0_30 = [x for x in range(0, 30)]
    lat_30_60 = [x for x in range(30, 60)]
    lat_60_90 = [x for x in range(60, 90)]

    lat_90_60_m = [x for x in range(-90, -60)]
    lat_60_30_m = [x for x in range(-60, -30)]
    lat_30_0_m = [x for x in range(-30, 0)]

    list_lat = (lat_0_30, lat_30_60, lat_60_90,
                lat_90_60_m, lat_60_30_m, lat_30_0_m)

    tm = []
    for i in list_lat:
        if x in i:
            tmp_x = (i[0], i[-1]+1)

    for i in list_lon:
        if y in i:
            tmp_y = (i[0], i[-1]+1)

    lst = (tmp_x[0], tmp_x[1], tmp_y[0], tmp_y[1])

    if x - tmp_x[0] < tmp_x[1] - x:
        tm.append(tmp_x[0])
    else:
        tm.append(tmp_x[1])

    if abs(y - tmp_y[0]) < abs(tmp_y[1] - y):
        tm.append(tmp_y[0])
    else:
        tm.append(tmp_y[1])

    final = []
    if tm[0] < 0:
        final.append(str(abs(tm[0])) + 'm')
    else:
        final.append(str(tm[0]))
    if tm[1] < 0:
        final.append(str(abs(tm[1])) + 'm')
    else:
        final.append(str(tm[1]))

    return final
