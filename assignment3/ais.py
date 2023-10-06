from loader import read_payloads
from transformer import as_timestamp_bitlist, as_dicts
from writer import write_tsv


def main(in_filenm, out_filenm):
    """
    A program to transform a logfile with raw AIS messages into a
    tab-separated text file readable with QGIS
    """
    payloads = read_payloads(in_filenm)
    lst = as_timestamp_bitlist(payloads)
    dict_list = as_dicts(lst)
    write_tsv(dict_list, out_filenm)


if __name__ == "__main__":
    # TODO: fix later
    main("./assignment3/aislog.txt", "./assignment3/aislogout.txt")
