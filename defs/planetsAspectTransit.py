# построение отсортированого списка аспектов планет

async def calc(_natal, _transit):
    n = 10
    m = 10
    # численные значения всех аспектов
    planetsAsp = [[0] * m for i in range(n)]
    planetsAspGui = [[0] * m for j in range(n)]
    list = []
    for x in range(len(_transit)):
        for y in range(len(planetsAsp)):
            planetsAsp[y][x] = asp(_transit[y], _natal[x])
            planetsAspGui[y][x] = tmasp(planetsAsp[y][x])
            k = str(x) + str(y)
            if planetsAspGui[y][x] == True:
                list.append(k)
    return (pops(list))

# Расчет аспекта планет


def asp(p1, p2):
    aspect = abs(p1 - p2)
    if aspect > 180:
        aspect = 360-aspect
    return aspect

# Создание списка мажорных транзитов планет


def tmasp(z):
    w = None
    if z > 180:
        z = 360 - z
    if 179 < z < 180:
        w = True  # оппозиция
    elif 119 < z < 121:
        w = True  # тригон
    elif 89 < z < 91:
        w = True  # квадратура
    elif 59 < z < 61:
        w = True  # секстиль
    elif 0 < z < 1:
        w = True  # соединение с др.планетами
    # elif z == 0: w = None  # соединение с самим собой
    return w

# очистка списка транзитных аспектов от зеркальных дубликатов


def pops(list1):
    list2 = []
    b = list(set([tuple(i) for i in map(sorted, list1)]))
    # не понятно. как сортирует ..  но удаляет зеркалки!
    l = len(b)
    for x in range(l):
        s = b[x][0] + b[x][1]
        list2.append(s)
    list2.sort()
    return list2
