from multiprocessing import Pool, Process, Lock
import multiprocessing as mp
from time import perf_counter
from defs.gradusPlanets import calc as gp

# _natal = [round(i, 1) for i in gp(1977, 5, 27, 12, 0, 0, 0, 0)]

lat = [i for i in range(-90, 91, 10)]
lon = [i for i in range(-180, 180, 10)]

lat = [-90, -80, -70, -60, -50, -40, -30, -20, -
       10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
lon = [-180, -170, -160, -150, -140, -130, -120, -110, -100, -90, -80, -70, -60, -50, -40, -
       30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]

# print(lon)
