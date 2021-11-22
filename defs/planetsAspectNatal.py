
async def calc(gp):  # gradusPlanets
    n = 10
    m = 10
    # численные значения всех аспектов
    planetsAsp = [[0] * m for i in range(n)]
    planetsAspGui = [[0] * m for j in range(n)]
    list = []
    for x in range(len(gp)):
        for y in range(len(planetsAsp)):
            planetsAsp[y][x] = asp(gp[y], gp[x])
            planetsAspGui[y][x] = masp(planetsAsp[y][x])
            k = str(x) + str(y)
            if planetsAspGui[y][x] == True:
                list.append(k)
    return (pops(list))


def calc2(gp):  # gradusPlanets
    n = 10
    m = 10
    # численные значения всех аспектов
    planetsAsp = [[0] * m for i in range(n)]
    planetsAspGui = [[0] * m for j in range(n)]

    for x in range(len(gp)):
        for y in range(len(planetsAsp)):
            planetsAsp[y][x] = asp(gp[y], gp[x])
            planetsAspGui[y][x] = aspGui(planetsAsp[y][x])
    return planetsAspGui


def asp(p1, p2):  # Расчет аспекта планет
    aspect = abs(p1 - p2)
    if aspect > 180:
        aspect = 360-aspect
    return aspect

# Создание списка графических мажорных аспектов планет


def masp(z):   # z = planetsAsp[y][x]
    aspect = None
    if z > 180:
        z = 360 - z
    if 174 < z < 180:
        aspect = True  # оппозиция
    elif 114 < z < 126:
        aspect = True  # тригон
    elif 84 < z < 96:
        aspect = True  # квадратура
    elif 54 < z < 66:
        aspect = True  # секстиль
    elif 0 < z < 6:
        aspect = True  # соединение с др.планетами
    elif z == 0:
        aspect = None  # соединение с самим собой
    return aspect

# Создание списка мажорных аспектов планет


def aspGui(z):
    w = None
    if z > 180:
        z = 360 - z
    if 174 < z < 180:
        w = '☍'  # оппозиция
    elif 114 < z < 126:
        w = '∆'  # тригон
    elif 84 < z < 96:
        w = '□'  # квадратура
    elif 54 < z < 66:
        w = '⚹'  # секстиль
    elif 0 < z < 6:
        w = '☌'  # соединение с др.планетами
    elif z == 0:
        w = None  # соединение с самим собой
    else:
        w = '-'  # если нет аспекта заполняем полем 0
    return w

# очистка списка аспектов от зеркальных дубликатов


def pops(list1):
    excl = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']
    list2 = []
    b = list(set([tuple(i) for i in map(sorted, list1)]))
    # не понятно. как сортирует ..  но удаляет зеркалки!
    l = len(b)
    for x in range(l):
        s = b[x][0] + b[x][1]
        if str(s) not in excl:
            list2.append(s)
    list2.sort()
    return list2
####################################################################


def pandas(gp):  # gradusPlanets
    n = 10
    m = 10
    # численные значения всех аспектов
    planetsAsp = [[0] * m for i in range(n)]
    planetsAspGui = [[0] * m for j in range(n)]
    list = []
    for x in range(len(gp)):
        for y in range(len(planetsAsp)):
            planetsAsp[y][x] = asp(gp[y], gp[x])
            planetsAspGui[y][x] = masp_pandas(planetsAsp[y][x])
    return (planetsAspGui)
