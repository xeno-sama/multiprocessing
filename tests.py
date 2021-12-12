from multiprocessing import Pool, Process, Lock
import multiprocessing as mp
from time import perf_counter
from defs.gradusPlanets import calc as gp

# _natal = [round(i, 1) for i in gp(1977, 5, 27, 12, 0, 0, 0, 0)]

lat = [i for i in range(-90, 91, 10)]
lon = [i for i in range(-180, 180, 10)]

x = [('data',), ('sun',), ('moon',), ('mercury',), ('venus',), ('mars',),
     ('jupiter',), ('saturn',), ('uranus',), ('neptune',), ('pluto',)]
tmp = [i[0] for i in x][:-1]
number = 6.56
print(round(number / 10) * 10)
