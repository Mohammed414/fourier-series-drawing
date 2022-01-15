from trapezoidal import trap_int
from utils import tiktok_function
from math import sqrt
import cmath

def get_constant(cn):
    c_sub_n = trap_int(0, 1, tiktok_function, 100, cn)
    # from a+bi to re^at
    # theta = round(cmath.phase(c_sub_n), 3)
    # r = round(sqrt((c_sub_n.real ** 2) + (c_sub_n.imag ** 2)), 3)
    # return r, theta
    return (round(c_sub_n.real, 4) + round(c_sub_n.imag, 4)*1j)