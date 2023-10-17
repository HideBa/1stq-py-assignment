# GEO1000 - Assignment 3
# Authors: Hidemichi Baba, Shawn Tew
# Studentnumbers: 5967538, 5925673


def write_tsv(lst, filenm_out):
    """
    Writes Tab Separated values to a file with name filenm_out

    Arguments:

        lst: list of dictionaries with the message content
             [{'msgtype': 1, ...}, {...}, ...]
        filenm_out: string specifying name of the file to use for output

    """
    DELIMITER = "\t"

    fields = (
        "timestamp",
        "msgtype",
        "repeat",
        "mmsi",
        "status",
        "turn",
        "speed",
        "accuracy",
        "lon",
        "lat",
        "course",
        "heading",
        "second",
        "maneuver",
        "raim",
        "radio",
    )

    with open(filenm_out, "w+") as file:
        # write first line with keys
        joined_keys = DELIMITER.join(fields) + "\n"
        file.write(joined_keys)

        tsv_body_str = ""
        for dict in lst:
            joined_values = (
                DELIMITER.join([str(dict[field]) for field in fields]) + "\n"
            )
            tsv_body_str += joined_values
        file.write(tsv_body_str)


def _test():
    # use this function to test your implementation
    pass


if __name__ == "__main__":
    _test()
