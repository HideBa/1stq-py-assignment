# GEO1000 - Assignment 2
# Authors: Hidemichi Baba
# Studentnumbers: 5967538

from math import radians, cos, sin, asin, sqrt


def haversin(latlon1, latlon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    arguments:
        latlon1 - tuple (lat, lon)
        latlon2 - tuple (lat, lon)

    returns:
        distance between the two coordinates (as float, *not* rounded)
    """
    phi1, lambda1 = latlon1
    phi2, lambda2 = latlon2
    delta_phi = phi2 - phi1
    delta_lambda = lambda2 - lambda1
    rad_phi1, rad_phi2, rad_lambda1, rad_lambda2, rad_delta_phi, rad_delta_lambda = (
        radians(phi1),
        radians(lambda1),
        radians(phi2),
        radians(lambda2),
        radians(delta_phi),
        radians(delta_lambda),
    )

    EARTH_RADIUS = 6371.0
    delta_sigma = (
        EARTH_RADIUS
        * 2
        * asin(
            sqrt(
                sin(rad_delta_phi / 2) * sin(rad_delta_phi / 2)
                + cos(rad_phi1) * cos(rad_phi2) * sin(rad_delta_lambda) / 2
            )
            * sin(rad_delta_lambda / 2)
        )
    )
    return delta_sigma


def _test():
    # You can use this function to test the distance calculation
    pass


if __name__ == "__main__":
    _test()
