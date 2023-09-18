# GEO1000 - Assignment 1
# Authors: Hidemichi Baba & Yan Gao
# Studentnumbers: 5967538, 6006175

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


# ax:number, ay:number, bx:number, by:number, cx:number, cy:number, alpha:number(degree), beta:number(degree)
# -> (px:number, py:number)
def tienstra(ax, ay, bx, by, cx, cy, alpha, beta):
    node_ab = distance(ax, ay, bx, by)
    node_bc = distance(bx, by, cx, cy)
    node_ac = distance(ax, ay, cx, cy)

    gamma = 360 - alpha - beta  # degree

    angle_a = angle(node_ab, node_ac, node_bc)
    angle_b = angle(node_ab, node_bc, node_ac)
    angle_c = angle(node_ac, node_bc, node_ab)

    k1 = k(angle_a, math.radians(alpha))
    k2 = k(angle_b, math.radians(beta))
    k3 = k(angle_c, math.radians(gamma))

    px = (k1 * ax + k2 * bx + k3 * cx) / (k1 + k2 + k3)
    py = (k1 * ay + k2 * by + k3 * cy) / (k1 + k2 + k3)

    # Because Python doesn't show the exact value of float, we use format() to show 10 digits after the decimal point.
    print("(Px, Py) is " + "(" + format(px, ".10f") + ", " + format(py, ".10f") + ")")

    return (px, py)


# Result(Px, Py) is (2082.1882960043, 5902.8525924374)
tienstra(1000.0, 5300.0, 2200.0, 6300.0, 3100.0, 5000.0, 115.052, 109.3045)

# Example of an own triangle. Expected (Px, Py) is (2.1930476110, 2.8386095222)
tienstra(1.0, 2.0, 4.0, 2.0, 2.0, 5.0, 120, 120)
