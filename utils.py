import math


def calc_distance(ax, ay, bx, by):
    dx = bx-ax
    dy = by-ay
    return math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
