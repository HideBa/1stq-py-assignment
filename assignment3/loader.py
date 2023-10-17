# GEO1000 - Assignment 3
# Authors: Hidemichi Baba, Shawn Tew
# Studentnumbers: 5967538, 5925673


def get_payload(raw_msg):
    """
    Returns tuple of payload and padding of a given raw AIS message

    For the raw AIS message:

        !AIVDM,1,1,1,A,13an?n002APDdH0Mb85;8'sn06sd,0*76

    the payload is:

        13an?n002APDdH0Mb85;8'sn06sd

    the padding (the digit before the *) is:

        0

    Returns:
        tuple (payload:str, padding:int)
    """
    *_, payload, right = raw_msg.split(",")
    padding, *_ = right.split("*")
    return (payload, int(padding))


def read_payloads(filenm):
    """
    Reads the AIS messages (timestamp, payload and padding) from the file

    Arguments:
        :filenm: name of the file to be opened

    Uses:
        get_payload to get the payload and padding from each raw AIS message

    Returns:
        A list with tuples:
        [(timestamp:str, payload:str, padding:int), ...]
    """
    ais_logs = []
    with open(filenm, "r") as file:
        lines = file.readlines()
        for line in lines:
            timestamp, raw_msg = line.split("\t")
            payload, padding = get_payload(raw_msg)
            ais_logs.append((timestamp, payload, padding))
    return ais_logs


def _test():
    # use this function to test your implementation
    pass


if __name__ == "__main__":
    _test()
