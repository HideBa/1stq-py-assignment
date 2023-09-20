# GEO1000 - Assignment 2
# Authors: Hidemichi Baba
# Studentnumbers: 5967538


from nominatim import nominatim

# from nominatim_offline import nominatim # can be used for testing if you are offline
# or if the online Nominatim service does not work
from dms import format_dd_as_dms
from distance import haversin


def query():
    """Query the WGS'84 coordinates of 2 places and compute the distance
        between them.

        A sample run of the program:

    I will find the distance for you between 2 places.
    Enter place 1? Delft
    Enter place 2? Bratislava
    Coordinates for Delft: N  51° 59' 58.0459", E   4° 21' 45.8083"
    Coordinates for Bratislava: N  48°  9'  6.1157", E  17°  6' 33.5027"
    The distance between Delft and Bratislava is 1003.4 km
    Enter place 1?
    Enter place 2? quit
    Bye bye.

        And another run:

    I will find the distance for you between 2 places.
    Enter place 1? where is this place?
    Enter place 2?
    I did not understand this place: where is this place?
    I did not understand this place:
    Enter place 1? quit
    Enter place 2?
    Bye bye.

    """
    print("`I will find the distance for you between 2 places.`")
    while True:
        user_input1 = input("Enter place 1?")
        user_input2 = input("Enter place 2?")
        if user_input1 == "quit" or user_input2 == "quit":
            print("Bye bye.")
            break

        if user_input1 == "" or user_input2 == "":
            print("you need to input name of city")
        coordinate1 = nominatim(user_input1)
        coordinate2 = nominatim(user_input2)
        print("loc1------", coordinate1)
        print("loc2------", coordinate2)
        if not (len(coordinate1) == 2 or len(coordinate2) == 2):
            continue

        print(
            "Coordinates for {}: {}".format(user_input1, format_dd_as_dms(coordinate1))
        )
        print(
            "Coordinates for {}: {}".format(user_input2, format_dd_as_dms(coordinate2))
        )

        distance = haversin(coordinate1, coordinate2)
        print(
            "The distance between {} and {} is {}km".format(
                user_input1, user_input2, distance
            )
        )


if __name__ == "__main__":
    query()
