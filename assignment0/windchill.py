# GEO1000 - Assignment 0
# Authors: Hidemichi Baba
# Studentnumbers: 5967538
# Assignement page url: https://brightspace.tudelft.nl/d2l/le/content/595998/viewContent/3511144/View


def temp_windchill(temp_in_c, windspeed_in_kmh):
    wind_chill_temperature = (
        13.12
        + 0.6215 * temp_in_c
        - 11.37 * windspeed_in_kmh**0.16
        + 0.3965 * temp_in_c * windspeed_in_kmh**0.16
    )
    return wind_chill_temperature


# result is 2.6584341521226054
temp_windchill(5.0, 10.0)
