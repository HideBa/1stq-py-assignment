# GEO1000 - Assignment 2
# Authors: Hidemichi Baba
# Studentnumbers: 5967538


def move(start, end, moves):
    if moves == 0 and start == end:
        return 1
    elif moves == 0 and start != end:
        return 0
    return move(start + 1, end, moves - 1) + move(start - 1, end, moves - 1)


if __name__ == "__main__":
    print("running robot.py directly")
    print(move(1, 4, 5))
    print(move(4, 1, 5))
    print(move(1, 4, 9))
    print(move(1, 4, 6))
    print(move(1, 4, 2))
