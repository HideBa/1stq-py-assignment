# GEO1000 - Assignment 1
# Authors: Hidemichi Baba
# Studentnumbers: 5967538

import math


def distance(x1, y1, x2, y2):
    return math.dist((x1, y1), (x2, y2))


# a,b,c: num(coordinate point) -> num(angle in radian between a,b)
def angle(a, b, c):
    r = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
    return r


def cot(x):
    return 1 / math.tan(x)


def k(angle_corner, angle_interior):
    # angle is in radian
    return 1 / (cot(angle_corner) - cot(angle_interior))


# alpha, beta, gamma are in degree
def tienstra(ax, ay, bx, by, cx, cy, alpha, beta):
    node_ab = distance(ax, ay, bx, by)
    node_bc = distance(bx, by, cx, cy)
    node_ac = distance(ax, ay, cx, cy)
    gamma = 360 - alpha - beta

    k1 = k(angle(node_ab, node_ac, node_bc), math.radians(alpha))
    k2 = k(angle(node_ab, node_bc, node_ac), math.radians(beta))
    k3 = k(angle(node_ac, node_bc, node_ab), math.radians(gamma))

    px = (k1 * ax + k2 * bx + k3 + cx) / (k1 + k2 + k3)
    py = (k1 * ay + k2 * by + k3 + cy) / (k1 + k2 + k3)
    print("(Px, Py) is " + "(" + str(px) + ", " + str(py) + ")")
    return (px, py)


# result is (255058.40780035098, 636068.8075068599)
tienstra(1000.0, 5300.0, 2200.0, 6300.0, 3100.0, 5000.0, 115.052, 109.3045)
