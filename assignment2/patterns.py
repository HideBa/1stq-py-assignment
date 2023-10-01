# GEO1000 - Assignment 2
# Authors: Hidemichi Baba, Shawn Tew
# Studentnumbers: 5967538, 5925673


def wkt(p1, p2, p3, p4):
    points = []  # [(p1[0], p1[1]), (p2[0], p2[1]), (p3[0], p3[1]), (p4[0], p4[1])
    for point in [p1, p2, p3, p4]:
        points.append(("{:.6f}".format(point[0]), "{:.6f}".format(point[1])))

    return "POLYGON (({x1} {y1}, {x2} {y2}, {x3} {y3}, {x4} {y4}, {x1} {y1}))".format(
        x1=points[0][0],
        y1=points[0][1],
        x2=points[1][0],
        y2=points[1][1],
        x3=points[2][0],
        y3=points[2][1],
        x4=points[3][0],
        y4=points[3][1],
    )


def pattern_a(level, center, size, ratio, file_nm):
    if level <= 0 or size < 0 or ratio < 0 or center is None or file_nm == "":
        return

    point1 = (center[0] - size, center[1] - size)
    point2 = (center[0] + size, center[1] - size)
    point3 = (center[0] + size, center[1] + size)
    point4 = (center[0] - size, center[1] + size)

    with open(file_nm, "a") as f:
        f.write("{};\n".format(wkt(point1, point2, point3, point4)))
    level = level - 1
    for point in [point1, point2, point3, point4]:
        pattern_a(level, point, size / ratio, ratio, file_nm)


def pattern_b(level, center, size, ratio, file_nm):
    if level <= 0 or size < 0 or ratio < 0 or center is None or file_nm == "":
        return

    point1 = (center[0] - size, center[1] - size)
    point2 = (center[0] + size, center[1] - size)
    point3 = (center[0] + size, center[1] + size)
    point4 = (center[0] - size, center[1] + size)
    level = level - 1
    for point in [point1, point2, point3, point4]:
        pattern_b(level, point, size / ratio, ratio, file_nm)
    with open(file_nm, "a") as f:
        f.write("{};\n".format(wkt(point1, point2, point3, point4)))


def pattern_c(level, center, size, ratio, file_nm):
    if level <= 0 or size < 0 or ratio < 0 or center is None or file_nm == "":
        return

    point1 = (center[0] - size, center[1] - size)
    point2 = (center[0] + size, center[1] - size)
    point3 = (center[0] + size, center[1] + size)
    point4 = (center[0] - size, center[1] + size)
    point1_2 = [point1, point2]
    point3_4 = [point3, point4]

    level = level - 1

    for point in point3_4:
        pattern_c(level, point, size / ratio, ratio, file_nm)

    with open(file_nm, "a") as f:
        f.write("{};\n".format(wkt(point1, point2, point3, point4)))

    for point in point1_2:
        pattern_c(level, point, size / ratio, ratio, file_nm)


def main(
    n=1, c=(0.0, 0.0), size=10.0, ratio=2.2
):  # note, optional arguments, see Sec 13.5 of ThinkPython2
    """The starting point of this program.
    Writes for every output file the first line and allows
    to influence how the resulting set of squares look.

    Arguments:
        n - levels of squares that will be produced
        c - coordinate of center of the drawing
        size - half side length of the first square
        ratio - how much smaller a square on the next level will be drawn

    """
    funcs = [pattern_a, pattern_b, pattern_c]
    file_nms = ["pattern_a.txt", "pattern_b.txt", "pattern_c.txt"]
    for func, file_nm_out in zip(funcs, file_nms):
        with open(file_nm_out, "w") as f:
            f.write("level;geometry\n")  # first line of the file
        func(level=n, center=c, size=size, ratio=ratio, file_nm=file_nm_out)


if __name__ == "__main__":
    main()
