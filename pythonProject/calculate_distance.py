from cmath import sin, cos
from math import atan2, radians
import numpy as np
# radius of the earth
R = 6371


def heuristik(location1, location2):
    lat1 = radians(location1[0])
    lat2 = radians(location2[0])
    lon1 = radians(location1[1])
    lon2 = radians(location2[1])
    lat_dif = lat2 - lat1
    lon_dif = lon2 - lon1
    a = (sin(lat_dif / 2) ** 2) + (cos(location1[0]) * cos(location2[0]) * (sin(lon_dif / 2) ** 2))
    c = 2 * atan2(np.sqrt(a), np.sqrt(1 - a))
    d = R * c
    return d


print(calculate((41.507483, -99.436554), (38.504048, -98.315949)))
