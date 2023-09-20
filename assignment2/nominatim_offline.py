# GEO1000 - Assignment 2
# Authors: Hidemichi Baba
# Studentnumbers: 5967538


def nominatim(place):
    """Geocode a place name, returns tuple with latitude, longitude
    returns empty tuple if no place found for the name given.

    This module gives a workaround for testing your code, without
    having a network connection (or not willing to use the online Nominatim
    service). It only 'knows' coordinates for 4 places, though.

    arguments:
        place - string

    returns:
        2-tuple of floats: (latitude, longitude) or
        empty tuple in case of failure
    """

    place_loc_dict = {
        "bratislava": (48.1516988, 17.1093063),
        "delft": (51.999457199999995, 4.362724538543995),
        "prague": (50.0596288, 14.446459273258009),
        "new york": (40.7127281, -74.0060152),
    }
    # If the palce does not exist in place_loc_dict, return an empty tuple
    loc = place_loc_dict.get(place.lower(), ())
    return loc


def _test():
    # Expected behaviour
    # unknown place leads to empty tuple
    # assert nominatim("unknown xxxyyy") == ()
    # delft leads to coordinates of delft
    assert nominatim("delft") == (51.999457199999995, 4.362724538543995)


if __name__ == "__main__":
    _test()
