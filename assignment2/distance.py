# GEO1000 - Assignment 2
# Authors: Hidemichi Baba, Shawn Tew
# Studentnumbers: 5967538, 5925673

from math import radians, cos, sin, asin, sqrt


def haversin(latlon1, latlon2):
    phi1, lambda1 = latlon1
    phi2, lambda2 = latlon2

    delta_phi = phi2 - phi1
    delta_lambda = lambda2 - lambda1

    EARTH_RADIUS = 6371.0
    delta_sigma = (
        EARTH_RADIUS
        * 2
        * asin(
            sqrt(
                sin(radians(delta_phi / 2)) * sin(radians(delta_phi / 2))
                + cos(radians(phi1))
                * cos(radians(phi2))
                * sin(radians(delta_lambda / 2))
                * sin(radians(delta_lambda / 2))
            )
        )
    )
    return delta_sigma


def _test():
    # You can use this function to test the distance calculation
    pass


if __name__ == "__main__":
    _test()
