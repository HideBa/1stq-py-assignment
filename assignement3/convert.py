# GEO1000 - Assignment 3
# Authors: Hidemichi Baba
# Studentnumbers: 5967538


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

    nrows = None
    ncols = None
    xllcorner = None
    yllcorner = None
    cellsize = None
    nodata_value = -9999
    data = None
    with open(file_nm, "r") as asc_file:
        file_content = asc_file.readlines()
        header_lines, body = file_content[:6], file_content[6:]
        for line in header_lines:
            if line.__contains__("NCOLS"):
                _, ncols_str = line.split(" ")
                ncols = int(ncols_str) if int(ncols_str) > 0 else None
            elif line.__contains__("NROWS"):
                _, nrows_str = line.split(" ")
                nrows = int(nrows_str) if int(nrows_str) > 0 else None
            elif line.__contains__("XLLCORNER"):
                _, xllcorner_str = line.split(" ")
                xllcorner = float(xllcorner_str)
            elif line.__contains__("YLLCORNER"):
                _, yllcorner_str = line.split(" ")
                yllcorner = float(yllcorner_str)
            elif line.__contains__("CELLSIZE"):
                _, cellsize_str = line.split(" ")
                cellsize = float(cellsize_str) if float(cellsize_str) > 0.0 else None
            elif line.__contains__("NODATA_VALUE"):
                _, nodata_value_str = line.split(" ")
                nodata_value = int(nodata_value_str)
        data = [[int(x) for x in line.split(" ") if x != "\n"] for line in body]
    return (nrows, ncols, xllcorner, yllcorner, cellsize, nodata_value, data)


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
    if cur_row <= 0 or cur_col <= 0:
        print("no!!!")
        return None

    nth_row_from_bottom = rows - cur_row
    x = xll + size * cur_col
    y = yll + size * nth_row_from_bottom
    return (x, y)


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
    virtual_cell_num = (rows - 1) * (cols - 1)  # e.g. there are 4 v-cells for 3x3

    coordinates = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            # TODO: consider no data value
            bottom_left = raster[i + 1][j]
            bottom_right = raster[i + 1][j + 1]
            top_right = raster[i][j + 1]
            top_left = raster[i][j]
            cell_index = (
                bottom_left * 1 + bottom_right * 2 + top_right * 4 + top_left * 8
            )
            cell_center = rowcol_to_xy_center(i + 1, j + 1, rows, cols, xll, yll, size)
            # TODO: check later
            if cell_center is None:
                return

            half_edge = size / 2
            coordinate = []
            if cell_index == 0 or cell_index == 15:
                continue
            elif cell_index == 1 or cell_index == 14:
                coordinate = [
                    (cell_center[0], cell_center[1] - half_edge),
                    (cell_center[0] - half_edge, cell_center[1]),
                ]
            elif cell_index == 2 or cell_index == 13:
                coordinate = [
                    (cell_center[0], cell_center[1] - half_edge),
                    (cell_center[0] + half_edge, cell_center[1]),
                ]
            elif cell_index == 3 or cell_index == 12:
                coordinate = [
                    (cell_center[0] - half_edge, cell_center[1]),
                    (cell_center[0] + half_edge, cell_center[1]),
                ]
            elif cell_index == 4 or cell_index == 11:
                coordinate = [
                    (cell_center[0] + half_edge, cell_center[1]),
                    (cell_center[0], cell_center[1] + half_edge),
                ]
            elif cell_index == 5:
                coordinate = [
                    [
                        (cell_center[0], cell_center[1] - half_edge),
                        (cell_center[0] + half_edge, cell_center[1]),
                    ],
                    [
                        (cell_center[0] - half_edge, cell_center[1]),
                        (cell_center[0], cell_center[1] + half_edge),
                    ],
                ]
            elif cell_index == 6 or cell_index == 9:
                coordinate = [
                    (cell_center[0], cell_center[1] - half_edge),
                    (cell_center[0], cell_center[1] + half_edge),
                ]
            elif cell_index == 7 or cell_index == 8:
                coordinate = [
                    (cell_center[0] - half_edge, cell_center[1]),
                    (cell_center[0], cell_center[1] + half_edge),
                ]
            elif cell_index == 10:
                coordinate = [
                    [
                        (cell_center[0], cell_center[1] - half_edge),
                        (cell_center[0] - half_edge, cell_center[1]),
                    ],
                    [
                        (cell_center[0] + half_edge, cell_center[1]),
                        (cell_center[0], cell_center[1] + half_edge),
                    ],
                ]
            coordinates.append(coordinate)
    print("coordinates: ", coordinates[0:20])
    return coordinates


def wkt(segment):
    """Get for a segment a Well Known Text string

    For the segment: [(x1,y1), (x2,y2)], the WKT string is:

    LINESTRING(x1 y1, x2 y2)

    segment -- a list with 2 tuples: [(x1,y1), (x2,y2)]
    returns -- str
    """
    # print("seg---", segment)
    return "LINESTRING({} {}, {} {});\n".format(
        segment[0][0], segment[0][1], segment[1][0], segment[1][1]
    )


def write_segments(segments, out_file_nm):
    """Write the generated segments to a file

    segments -- list of segments: [[(x1,y1), (x2,y2)], ...]
    out_file_nm -- str

    returns -- None
    """
    segments_str = ""
    for segment in segments:
        wkt_str = wkt(segment)
        segments_str += wkt_str
    with open(out_file_nm, "w+", encoding="utf-8") as file:
        file.write(segments_str)


def convert(file_nm_in, file_nm_out):
    """Convert raster file to segments

    file_nm -- input file name as string
    returns -- None
    """
    (rows, cols, xll, yll, size, nodataval, data) = read_asc(file_nm_in)
    segments = marching_squares(rows, cols, xll, yll, size, nodataval, data)
    write_segments(segments, file_nm_out)


def main():
    """Starting point of the program, asks user for the name of the input file."""
    # convert(input("Which file to convert? >>> "), input("Name for output file?  >>> "))
    # convert("./assignement3/giraffe.asc", "./assignement3/giraffe.wkt")
    # convert("./assignement3/holland.asc", "./assignement3/holland.wkt")
    # convert("./assignement3/snail.asc", "./assignement3/snail.wkt")
    print("Done, result stored to out.wkt")


if __name__ == "__main__":
    main()
