# GEO1000 - Assignment 2
# Authors: Hidemichi Baba
# Studentnumbers: 5967538


from nominatim import nominatim

# from nominatim_offline import nominatim # can be used for testing if you are offline
# or if the online Nominatim service does not work
from dms import format_dd_as_dms
from distance import haversin


def query():
    print("I will find the distance for you between 2 places.")
    while True:
        user_input1 = input("Enter place 1?")
        user_input2 = input("Enter place 2?")
        if user_input1 == "quit" or user_input2 == "quit":
            print("Bye bye.")
            break

        if user_input1 == "" or user_input2 == "":
            # TODO: check what is expected behaviour
            print("you need to input name of city")
        coordinate1 = nominatim(user_input1)
        coordinate2 = nominatim(user_input2)

        # TODO: check geo-coding result is a little bit different
        if not (len(coordinate1) == 2 and len(coordinate2) == 2):
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
                user_input1, user_input2, "{:.1f}".format(distance)
            )
        )


if __name__ == "__main__":
    query()
