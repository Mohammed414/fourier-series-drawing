# import numpy as np
# import matplotlib.pyplot as plt

from svg_path import COORDINATES
from math import cos, sin, pi, e

# def plot_coordinates(coordinates_list):
#     data = np.array(coordinates_list)
#     x, y = data.T
#     plt.scatter(x,y)
#     plt.show()

def tiktok_function(t, cn):
    if t > 1:
        raise ValueError("t must be 0<= t <= 1 ")
    Z_coord = complex(COORDINATES[int(t*100)][0], COORDINATES[int(t*100)][1])
    value =  Z_coord * (e**(-2 * cn * pi * 1j * t))
    return value

def get_template(n, c_n):
    n_sub = str(n)
    if n < 0:
        n_sub = str((n*-1)) + "m" 

    template = r"r_{" + n_sub \
        +r"}=" + str(c_n[0]) \
            + r"\left(\left(\cos\left(2\pi\cdot "+ str(n) \
                +r"\cdot t\ +\ " + str(c_n[1])\
                    +r"\right),\ \sin\left(2\pi\cdot "+ str(n)+\
                         r"\cdot t\ +\ "+str(c_n[1])\
                             +r"\right)\right)\right)"
    return template