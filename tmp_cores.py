from multiprocessing import Pool, Process, Lock
import multiprocessing as mp
from time import perf_counter
from def_eph import test
from defs.gradusPlanets import calc as gp

start_time = perf_counter()
##############################

tmp = []


# def sum(s):
#     with open('test.txt', 'a') as f:
#         sum = 0
#         for item in range(s):
#             sum += item
#         tmp.append(sum)
#         f.write(str(tmp)+'\n')

def sum(s):

    sun = gp(1977, 5, s,
             12, 0, 0, 0.0, 0.0)[0]
    moon = gp(2021, 1, s,
              12, 0, 0, 0.0, 0.0)[1]
    mercury = gp(2021, 1, s,
                 12, 0, 0, 0.0, 0.0)[2]
    venus = gp(2021, 1, s,
               12, 0, 0, 0.0, 0.0)[3]
    mars = gp(2021, 1, s,
              12, 0, 0, 0.0, 0.0)[4]
    jupiter = gp(2021, 1, s,
                 12, 0, 0, 0.0, 0.0)[5]
    saturn = gp(2021, 1, s,
                12, 0, 0, 0.0, 0.0)[6]
    uranus = gp(2021, 1, s,
                12, 0, 0, 0.0, 0.0)[7]
    neptune = gp(2021, 1, s,
                 12, 0, 0, 0.0, 0.0)[8]
    pluto = gp(2021, 1, s,
               12, 0, 0, 0.0, 0.0)[9]

    print(sun)


def main():

    p1 = Process(target=sum, args=(1, ))
    p1.start()

    p2 = Process(target=sum, args=(2, ))
    p2.start()

    # p3 = Process(target=sum, args=(i+2, ))
    # p3.start()

    # p4 = Process(target=sum, args=(i+3, ))
    # p4.start()

    # p5 = Process(target=sum, args=(500000001, ))
    # p5.start()

    # p6 = Process(target=sum, args=(500000002, ))
    # p6.start()

    # p7 = Process(target=sum, args=(500000000, ))
    # p7.start()

    # p8 = Process(target=sum, args=(500000001, ))
    # p8.start()

    p1.join()
    p2.join()
    # p3.join()
    # p4.join()
    # p5.join()
    # p6.join()
    # p7.join()
    # p8.join()


if __name__ == '__main__':

    main()
    print(f'{(perf_counter() - start_time)}')

#############################

# def sum(s):

#     sun = gp(1977, 5, s,
#              12, 0, 0, 0.0, 0.0)[0]
#     moon = gp(2021, 1, s,
#               12, 0, 0, 0.0, 0.0)[1]
#     mercury = gp(2021, 1, s,
#                  12, 0, 0, 0.0, 0.0)[2]
#     venus = gp(2021, 1, s,
#                12, 0, 0, 0.0, 0.0)[3]
#     mars = gp(2021, 1, s,
#               12, 0, 0, 0.0, 0.0)[4]
#     jupiter = gp(2021, 1, s,
#                  12, 0, 0, 0.0, 0.0)[5]
#     saturn = gp(2021, 1, s,
#                 12, 0, 0, 0.0, 0.0)[6]
#     uranus = gp(2021, 1, s,
#                 12, 0, 0, 0.0, 0.0)[7]
#     neptune = gp(2021, 1, s,
#                  12, 0, 0, 0.0, 0.0)[8]
#     pluto = gp(2021, 1, s,
#                12, 0, 0, 0.0, 0.0)[9]

#     return sun


# def f(x):
#     return sum(x)


# if __name__ == '__main__':
#     with Pool(1) as p:
#         print(p.map(f, [x for x in range(27, 30)]))
#         print(f'{(perf_counter() - start_time)}')


########

# start_time = perf_counter()

# def sum(s):
#     sum = 0
#     for item in range(s):
#         sum += item
#     return sum


# def f(x):
#     return sum(x)


# if __name__ == '__main__':
#     with Pool(4) as p:
#         print(
#             p.map(f, [100000000, 100000002, 100000003, 100000004]))
#         print(f'{(perf_counter() - start_time)}')

########


# def sum(s):
#     sum = 0
#     for item in range(s):
#         sum += item
#     tmp.append(sum)
#     print(tmp)


# def main():
#     with open('test.txt', 'a') as f:

#         p1 = Process(target=sum, args=(50000000, ))
#         p1.start()
#         f.write(str(p1)+'\n')

#         p2 = Process(target=sum, args=(50000001, ))
#         p2.start()
#         f.write(str(p2)+'\n')

#         p3 = Process(target=sum, args=(50000002, ))
#         p3.start()
#         f.write(str(p3)+'\n')

#         p1.join()
#         p2.join()
#         p3.join()


# if __name__ == '__main__':

#     main()
#     print(f'{(perf_counter() - start_time)}')
