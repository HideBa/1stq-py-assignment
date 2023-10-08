# GEO1000 - Assignment 3
# Authors: Hidemichi Baba
# Studentnumbers: 5967538

from bitlist import BitList


def as_timestamp_bitlist(lst):
    """
    Transforms a list with:
      [(timestamp0, payload0, padding0), ..., (timestampn, payloadn, paddingn)]
    into a list with:
      [(timestamp0:str, bitlist0:BitList), ...]

    Returns:
        list with tuples
    """

    timestamp_bitlist = []
    for timestamp, payload, padding in lst:
        bit_list = BitList(payload, padding)
        timestamp_bitlist.append((timestamp, bit_list))
    return timestamp_bitlist


def as_dicts(lst):
    """
    Transforms a list with:
      [(timestamp0:str, bitlist0:BitList), ...]
    into:
      [{'msgtype': 1, ...}, ...]

    Uses:
      decode_msg_dict, postprocess_msg_dict

    Returns:
        list with dictionaries
    """
    dict_list = []
    for item in lst:
        decoded_msg = decode_msg_dict(item[0], item[1])
        processed_msg = postprocess_msg_dict(decoded_msg)
        dict_list.append(processed_msg)
    return dict_list


def decode_msg_dict(timestamp, bitlist):
    """
    Decode a BitList instance to a dictionary

    Arguments:
        timestamp: str
        bitlist: BitList instance

    Returns:
        Dictionary with keys/values: timestamp and all fields
        for the position message

    **Note, values of the fields are all (signed or unsigned) integers!**
    """
    msgtype = bitlist.ubits(0, 6)
    repeat = bitlist.ubits(6, 2)
    mmsi = bitlist.ubits(8, 30)
    status = bitlist.ubits(38, 4)
    turn = bitlist.sbits(42, 8)
    speed = bitlist.ubits(50, 10)
    accuracy = bitlist.ubits(60, 1)
    lon = bitlist.sbits(61, 28)
    lat = bitlist.sbits(89, 27)
    course = bitlist.ubits(116, 12)
    heading = bitlist.ubits(128, 9)
    second = bitlist.ubits(137, 6)
    maneuver = bitlist.ubits(143, 2)
    _ = bitlist.ubits(145, 3)  # spare
    raim = bitlist.ubits(148, 1)
    radio = bitlist.ubits(149, 19)
    dict = {
        "msgtype": msgtype,
        "repeat": repeat,
        "mmsi": mmsi,
        "status": status,
        "turn": turn,
        "speed": speed,
        "accuracy": accuracy,
        "lon": lon,
        "lat": lat,
        "course": course,
        "heading": heading,
        "second": second,
        "maneuver": maneuver,
        "raim": raim,
        "radio": radio,
        "timestamp": timestamp,  # TODO: check if timestamp is string or int
    }
    return dict


def postprocess_msg_dict(msg):
    """
    Modifier function, post processes the fields:
        speed, lon, lat, course and heading

    Arguments:
        msg: dict (with all fields + timestamp of position message)

    Uses:
        functions: div10 and geo

    Returns:
        None
    """
    msg["speed"] = div10(msg["speed"])
    msg["lon"] = geo(msg["lon"])
    msg["lat"] = geo(msg["lat"])
    msg["course"] = div10(msg["course"])
    msg["heading"] = div10(msg["heading"])
    return msg


def div10(field):
    """
    Divide a field by 10.0
    """
    return field / 10.0


def geo(field):
    """
    Divide field by 600000.0 and rounds to 5
    """
    return round(field / 600000.0, 5)


def _test():
    # use this function to test your implementation
    pass


if __name__ == "__main__":
    bit_list = BitList("000111", 0)
    print("bit---", bit_list.ubits(0, 6))
    print("bit---", bit_list.sbits(0, 6))
    _test()
