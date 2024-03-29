# GEO1000 - Assignment 4
# Authors:
# Student numbers:

# no other imports allowed than given
import math, sys
from geometry import Point, Circle, Triangle
import cProfile


class DelaunayTriangulation:
    def __init__(self, points):
        """Constructor"""
        self.triangles = []
        self.points = points

    def triangulate(self):
        """Triangulates the given set of points.

        This method takes the set of points to be triangulated
        (with at least 3 points) and for each 3-group of points instantiates
        a triangle and checks whether the triangle conforms to Delaunay
        criterion. If so, the triangle is added to the triangle list.

        To determine the 3-group of points, the group3 function is used.

        Returns None
        """
        # pre-condition: we should have at least 3 points
        assert len(self.points) > 2
        groups = group3(len(self.points))
        for group in groups:
            tri = Triangle(
                self.points[group[0]], self.points[group[1]], self.points[group[2]]
            )
            if self.is_delaunay(tri):
                self.triangles.append(tri)

    def is_delaunay(self, tri):
        """Does a triangle *tri* conform to the Delaunay criterion?

        Algorithm:

        Are 3 points of the triangle collinear?
            No:
                Get circumcircle
                Count number of points inside circumcircle
                if number of points inside == 3:
                    Delaunay
                else:
                    not Delaunay
            Yes:
                not Delaunay

        Arguments:
            tri -- Triangle instance
        Returns:
            True/False
        """
        is_collinear = self.are_collinear(tri.p0, tri.p1, tri.p2)
        if is_collinear:
            return False
        else:
            circumcircle = tri.circumcircle()
            count = 0
            for point in self.points:
                if circumcircle.covers(point):
                    count += 1
            if count == 3:
                return True
            else:
                return False

    def are_collinear(self, pa, pb, pc):
        """Orientation test to determine whether 3 points are collinear
        (on straight line).

        Note that we consider points that are nearly collinear also to be on
        a straight line (arbitrary epsilon to use: 1e-8).

        Returns True / False
        """
        ax, ay = pa.x, pa.y
        bx, by = pb.x, pb.y
        cx, cy = pc.x, pc.y
        result = (ax - cx) * (by - cy) - (bx - cx) * (ay - cy)
        return abs(result) < 1e-8

    def output_points(self, open_file_obj):
        """Outputs the points of the triangulation to an open file."""
        open_file_obj.write("wkt\n")
        for point in self.points:
            open_file_obj.write(point.as_wkt() + "\n")

    def output_triangles(self, open_file_obj):
        """Outputs the triangles of the triangulation to an open file."""
        open_file_obj.write("wkt\ttriangle_id\tarea\tperimeter\n")
        for tri in self.triangles:
            open_file_obj.write(
                "{wkt}\t{id}\t{area}\t{perimeter}\n".format(
                    wkt=tri.as_wkt(),
                    id=id(tri),
                    area=tri.area(),
                    perimeter=tri.perimeter(),
                )
            )

    def output_circumcircles(self, open_file_obj):
        """Outputs the circumcircles of the triangles of the triangulation
        to an open file
        """
        open_file_obj.write("wkt\ttriangle_id\tarea\tperimeter\n")
        for tri in self.triangles:
            circle = tri.circumcircle()
            open_file_obj.write(
                "{wkt}\t{id}\t{area}\t{perimeter}\n".format(
                    wkt=circle.as_wkt(),
                    id=id(tri),
                    area=circle.area(),
                    perimeter=circle.perimeter(),
                )
            )


def group3(N):
    """Returns generator with 3-tuples with indices to form 3-groups
    of a list of length N.

    Total number of tuples that is generated: N! / (3! * (N-3)!)

    For N = 3: [(0, 1, 2)]
    For N = 4: [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    For N = 5: [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3),
                (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4),
                (1, 3, 4), (2, 3, 4)]

    Example use:

        >>> for item in group3(3):
        ...     print(item)
        ...
        (0, 1, 2)

    """
    # See for more information about generators for example:
    # http://web.archive.org/https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                yield (i, j, k)


def make_random_points(n):
    """Makes n points distributed randomly in x,y between [0,1000]

    Note, no duplicate points will be created, but might result in slightly
    less than the n number of points requested.
    """
    import random

    # seed the random generator, so we still get a random set of points,
    # but each time the same set of randomized ones
    random.seed(2023)
    pts = list(
        set([Point(random.randint(0, 1000), random.randint(0, 1000)) for i in range(n)])
    )
    return pts


def main(n):
    """Perform triangulation of n points and write the resulting geometries
    to text files, where the geometry is stored as well-known text strings.
    """
    pts = make_random_points(n)
    dt = DelaunayTriangulation(pts)
    dt.triangulate()
    # using the with statement, we do not need to close explicitly the file
    with open(f"./assignment4/py/points_{n}.wkt", "w") as fh:
        dt.output_points(fh)
    with open(f"./assignment4/py/triangles_{n}.wkt", "w") as fh:
        dt.output_triangles(fh)
    with open(f"./assignment4/py/circumcircles_{n}.wkt", "w") as fh:
        dt.output_circumcircles(fh)


def print_error():
    """Prints an eror when a script parameter is missing on the command line"""
    print("ERROR: Call this script with an integer as script parameter")
    print("to set the number of points for the triangulation.")
    print(f"Example: $ python {sys.argv[0]} 100")


def _test():
    # If you want, you can write tests in this function
    pass  # Your implementation here


if __name__ == "__main__":
    print("This is the name of the Python script:", sys.argv[0])
    print("Number of arguments:", len(sys.argv))
    print("The arguments are:", str(sys.argv))
    if len(sys.argv) != 2:
        print_error()
    else:
        try:
            point_count = int(sys.argv[1])
            print("Running triangulation...")
            # TODO: remove me after perfomance testing
            cProfile.run("main(point_count)", sort="cumtime", filename="profile")
            # main(point_count)
            print("done.")
        except ValueError:
            print_error()
            raise
