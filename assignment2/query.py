# GEO1000 - Assignment 2
# Authors: Hidemichi Baba
# Studentnumbers: 5967538


from nominatim import nominatim
from dms import format_dd_as_dms
from distance import haversin


def query():
    print("I will find the distance for you between 2 places.")

    while True:
        user_input1 = input("Enter place 1? ")
        user_input2 = input("Enter place 2? ")
        if user_input1 == "quit" or user_input2 == "quit":
            print("Bye bye.")
            break

        coordinate1 = nominatim(user_input1)
        coordinate2 = nominatim(user_input2)

        if not (len(coordinate1) == 2 or len(coordinate2) == 2):
            print("I did not understand this place: {}".format(user_input1))
            print("I did not understand this place: {}".format(user_input2))
            continue

        print(
            "Coordinates for {}: {}".format(user_input1, format_dd_as_dms(coordinate1))
        )
        print(
            "Coordinates for {}: {}".format(user_input2, format_dd_as_dms(coordinate2))
        )

        distance = haversin(coordinate1, coordinate2)
        print(
            "The distance between {} and {} is {} km".format(
                user_input1, user_input2, "{:.1f}".format(distance)
            )
        )


if __name__ == "__main__":
    query()
