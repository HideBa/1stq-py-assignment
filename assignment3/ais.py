# GEO1000 - Assignment 3
# Authors: Hidemichi Baba, Shawn Tew
# Studentnumbers: 5967538, 5925673

from loader import read_payloads
from transformer import as_timestamp_bitlist, as_dicts
from writer import write_tsv


def main(in_filenm, out_filenm):
    """
    A program to transform a logfile with raw AIS messages into a
    tab-separated text file readable with QGIS
    """
    payloads = read_payloads(in_filenm)
    timestamp_bits = as_timestamp_bitlist(payloads)
    dicts = as_dicts(timestamp_bits)
    write_tsv(dicts, out_filenm)


if __name__ == "__main__":
    main("./assignment3/aislog.txt", "./assignment3/aislogout.txt")
