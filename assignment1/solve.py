# GEO1000 - Assignment 1
# Authors: Hidemichi Baba & Yan Gao
# Studentnumbers: 5967538, 6006175

from math import sqrt

TEXT1 = "The roots of "


# return result for testability
def abc(a, b, c):
    d = discriminant(a, b, c)
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print(
            TEXT1
            + str(a)
            + "x^2 + "
            + str(b)
            + "x "
            + "+ "
            + str(c)
            + " are: "
            + "x1 = "
            + str(x1)
            + ", x2 = "
            + str(x2)
        )
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        if x == -0.0:  # Because Python has -0.0 and 0.0
            x = 0.0
        print(
            TEXT1
            + str(a)
            + "x^2 + "
            + str(b)
            + "x "
            + "+ "
            + str(c)
            + " are: "
            + "x = "
            + str(x)
        )
        return x
    else:
        result = "not real"
        print(
            TEXT1
            + str(a)
            + "x^2 + "
            + str(b)
            + "x "
            + "+ "
            + str(c)
            + " are: "
            + result
        )
        return result


# a,b,c: num -> num
def discriminant(a, b, c):
    d = b**2 - 4 * a * c
    return d


abc(2.0, 0.0, 0.0)
abc(1.0, 3.0, 2.0)
abc(3.0, 4.5, 9.0)
# output
# The roots of 2.0x^2 + 0.0x + 0.0 are: x = 0.0
# The roots of 1.0x^2 + 3.0x + 2.0 are: x1 = -1.0, x2 = -2.0
# The roots of 3.0x^2 + 4.5x + 9.0 are: not real
