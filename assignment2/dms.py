# GEO1000 - Assignment 2
# Authors: Hidemichi Baba
# Studentnumbers: 5967538


# num -> (num, num, num)
def dd_dms(decdegrees):
    """Returns tuple (degrees, minutes, seconds) for a value in decimal degrees

    Arguments:

    decdegrees -- float that represents a latitude or longitude value

    returns:

    3-tuple of *not* rounded floats (degrees, minutes, seconds)
    """
    min, sec = divmod(abs(decdegrees) * 3600, 60)
    degree, min = divmod(min, 60)
    # Return minus degree if it's minus
    degree = degree if decdegrees >= 0 else -1 * degree
    # TODO: check later
    return (degree, min, sec)


def format_dms(dms, is_latitude):
    """Returns a formatted string for *one* part of the coordinate.

    Arguments:

    dms -- tuple of floats (degrees, minutes, seconds)
           that represents a latitude or longitude value
    is_latitude -- boolean that specifies whether ordinate is latitude or longitude

    If is_latitude == True dms represents latitude (north/south)
    If is_latitude == False dms represents longitude (east/west)

    returns:

    Formatted string
    """
    # N   0°  0'  0.0000", E   0°  0'  0.0000"
    # N  52°  0'  0.0000", E   4° 19' 43.3200"
    template = "{}{:4}°{:3}'{:>8.4f}\""
    if is_latitude:
        north_south = "N" if dms[0] >= 0 else "S"
        return template.format(north_south, int(abs(dms[0])), int(dms[1]), dms[2])
    else:
        east_west = "E" if dms[0] >= 0 else "W"
        return template.format(east_west, int(abs(dms[0])), int(dms[1]), dms[2])


def format_dd_as_dms(coordinate):
    lat, lng = dd_dms(coordinate[0]), dd_dms(coordinate[1])
    lat_text, lng_text = format_dms(lat, True), format_dms(lng, False)
    return "{}, {}".format(lat_text, lng_text)


def _test():
    """Test whether the format_dd_as_dms function works correctly

        Expected output:

    N   0°  0'  0.0000", E   0°  0'  0.0000"
    N  52°  0'  0.0000", E   4° 19' 43.3200"
    S  52°  0'  0.0000", E   4° 19' 43.3200"
    N  52°  0'  0.0000", W   4° 19' 43.3200"
    S  52°  0'  0.0000", W   4° 19' 43.3200"
    N  45°  0'  0.0000", E 180°  0'  0.0000"
    S  45°  0'  0.0000", W 180°  0'  0.0000"
    S  50° 27' 24.1200", E   4° 19' 43.3200"

        (note, in PyCharm you can view the whitespace characters in a text file
         by switching on the option View → Active Editor → Show Whitespace)
    """
    coordinates = (
        (0.0, 0.0),
        (52.0, 4.3287),
        (-52.0, 4.3287),
        (52.0, -4.3287),
        (-52.0, -4.3287),
        (45.0, 180.0),
        (-45.0, -180.0),
        (-50.4567, 4.3287),
    )
    for coordinate in coordinates:
        print(format_dd_as_dms(coordinate))


if __name__ == "__main__":
    _test()
