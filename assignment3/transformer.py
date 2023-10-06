# GEO1000 - Assignment 3
# Authors:
# Studentnumbers:

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
    char_bit_dict = {
        "0": "000000",
        "1": "000001",
        "2": "000010",
        "3": "000011",
        "4": "000100",
        "5": "000101",
        "6": "000110",
        "7": "000111",
        "8": "001000",
        "9": "001001",
        ":": "001010",
        ";": "001011",
        "<": "001100",
        "=": "001101",
        ">": "001110",
        "?": "001111",
        "@": "010000",
        "A": "010001",
        "B": "010010",
        "C": "010011",
        "D": "010100",
        "E": "010101",
        "F": "010110",
        "G": "010111",
        "H": "011000",
        "I": "011001",
        "J": "011010",
        "K": "011011",
        "L": "011100",
        "M": "011101",
        "N": "011110",
        "O": "011111",
        "P": "100000",
        "Q": "100001",
        "R": "100010",
        "S": "100011",
        "T": "100100",
        "U": "100101",
        "V": "100110",
        "W": "100111",
        "’": "101000",
        "a": "101001",
        "b": "101010",
        "c": "101011",
        "d": "101100",
        "e": "101101",
        "f": "101110",
        "g": "101111",
        "h": "110000",
        "i": "110001",
        "j": "110010",
        "k": "110011",
        "l": "110100",
        "m": "110101",
        "n": "110110",
        "o": "110111",
        "p": "111000",
        "q": "111001",
        "r": "111010",
        "s": "111011",
        "t": "111100",
        "u": "111101",
        "v": "111110",
        "w": "111111",
    }

    timestamp_bitlist = []
    for timestamp, payload, padding in lst:
        bit_char = ""
        for char in payload:
            if char not in char_bit_dict:
                # TODO: check when char contains "`"
                continue
            bits = char_bit_dict[char]
            bit_char += bits
        bit_list = BitList(bit_char, padding)  # TODO: add padding
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
