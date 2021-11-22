# построение списка диспозиций планет учитывая натал ретро

async def calc(_natal, _velo):
    pos2 = []  # список диспозиторов
    for i in range(len(_natal)):  # len(planets)
        gradus = float(_natal[i])
        if 0 < gradus < 30:
            if _velo[4] == -1:
                pos2.append(str(i) + str(4))
            elif _velo[9] == 1:
                pos2.append(str(i) + str(9))
        elif 30 < gradus < 60:
            pos2.append(str(i) + str(3))
        elif 60 < gradus < 90:
            pos2.append(str(i) + str(2))
        elif 90 < gradus < 120:
            pos2.append(str(i) + str(1))
        elif 120 < gradus < 150:
            pos2.append(str(i) + str(0))
        elif 150 < gradus < 180:
            pos2.append(str(i) + str(2))
        elif 180 < gradus < 210:
            pos2.append(str(i) + str(3))
        elif 210 < gradus < 240:
            if _velo[4] == 1:
                pos2.append(str(i) + str(4))
            elif _velo[9] == -1:
                pos2.append(str(i) + str(9))
        elif 240 < gradus < 270:
            if _velo[5] == 1:
                pos2.append(str(i) + str(5))
            elif _velo[8] == -1:
                pos2.append(str(i) + str(8))
        elif 270 < gradus < 300:
            if _velo[6] == 1:
                pos2.append(str(i) + str(6))
            elif _velo[7] == -1:
                pos2.append(str(i) + str(7))
        elif 300 < gradus < 330:
            if _velo[6] == -1:
                pos2.append(str(i) + str(6))
            elif _velo[7] == 1:
                pos2.append(str(i) + str(7))
        elif 330 < gradus < 360:
            if _velo[5] == -1:
                pos2.append(str(i) + str(5))
            elif _velo[8] == 1:
                pos2.append(str(i) + str(8))
    return popsDisp(pos2)  # pos2

# очистка списка аспектов от зеркальных дубликатов


def popsDisp(list1):
    excl = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']
    list2 = []
    for x in range(len(list1)):
        s = list1[x]

        if s not in excl:
            if int(s[0]) < int(s[1]):
                list2.append(s)
            else:
                list2.append(s[1] + s[0])

    list2.sort()
    return list2

    # b = list(set([tuple(i) for i in map(sorted, list1)]))
    # # не понятно. как сортирует ..  но удаляет зеркалки!
    # l = len(b)
    # for x in range(l):
    #     s = b[x][0] + b[x][1]
    #     if str(s) not in excl:  list2.append(s)
    # list2.sort()
    # return list2
