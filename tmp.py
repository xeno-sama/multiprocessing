from datetime import date, datetime, timedelta
from const import *

date_start = date(year=1930, month=1, day=1)
x = [i for i in range(180, -180, -30)]

y = tuple([1.0 for i in range(3)])
data = str(date_start)
z = (data, y)
# dz = tuple([z[0]] + list(z[1]))
dz = tuple([data] + list(y))

print(dz)

# s = tuple(j for i in (('aa', 'bb', 'cc'), data)
#           for j in (i if isinstance(i, tuple) else (i,)))

# print(s)
# for i in x:
#     ix += 1
#     for j in y:
#         jy += 1
#         a[ix][jy] = i+j

#         # print(a[ix][jy])
#     jy = -1
# print(a)
