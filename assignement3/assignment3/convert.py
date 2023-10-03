# GEO1000 - Assignment 3
# Authors:
# Studentnumbers:


def read_asc(file_nm):
    """Read the ESRI ASCII grid file.

      arguments:
        file_nm -- name of the file to be read

      returns -- tuple with:
        (nrows, ncols, xllcorner, yllcorner, cellsize, nodata_value, data)
        where:
            nrows -- int
            ncols -- int
            xllcorner -- float
            yllcorner -- float
            cellsize -- float
            nodata_value -- int
            data -- list of lists, with integers
    """
    pass


def rowcol_to_xy_center(cur_row, cur_col, rows, cols, xll, yll, size):
    """Transform coordinates from top-down, to bottom-up coordinate system.
    The world coordinate returned should represent the center of the cell.

      arguments:
        cur_row -- int
        cur_col -- int
        rows -- int, number of rows in raster
        cols -- int, number of cols in raster
        xll -- float, x coordinate of lower left corner
        yll -- float, y coordinate of lower left corner
        size -- float, cellsize
    
      returns:
        (x, y) tuple
        where:
            x -- float
            y -- float
    """
    pass


def marching_squares(rows, cols, xll, yll, size, nodataval, raster):
    """Perform raster-vector conversion using marching squares algorithm.

      arguments:
        nrows -- int
        ncols -- int
        xll -- float
        yll -- float
        size -- float
        nodataval -- int
        raster -- list of lists, with integers

      returns:
        list of segments: [[(x1,y1), (x2,y2)], ..., [(xm,ym), (xn,yn)]]
    """
    pass


def wkt(segment):
    """Get for a segment a Well Known Text string

    For the segment: [(x1,y1), (x2,y2)], the WKT string is:

    LINESTRING(x1 y1, x2 y2)

    segment -- a list with 2 tuples: [(x1,y1), (x2,y2)]
    returns -- str
    """
    pass


def write_segments(segments, out_file_nm):
    """Write the generated segments to a file

    segments -- list of segments: [[(x1,y1), (x2,y2)], ...]
    out_file_nm -- str

    returns -- None
    """
    pass


def convert(file_nm_in, file_nm_out):
    """Convert raster file to segments

    file_nm -- input file name as string
    returns -- None
    """
    (rows, cols, xll, yll, size, nodataval, data) = read_asc(file_nm_in)
    segments = marching_squares(rows, cols, xll, yll, size, nodataval, data)
    write_segments(segments, file_nm_out)


def main():
    """Starting point of the program, asks user for the name of the input file.
    """
    convert(input("Which file to convert? >>> "),
            input("Name for output file?  >>> "))
    print("Done, result stored to out.wkt")


if __name__ == "__main__":
    main()
