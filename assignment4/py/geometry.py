# GEO1000 - Assignment 4
# Authors:
# Student numbers:

# no other imports allowed than given
import math


class Point:
    """Point, with x- and y-coordinate"""

    def __init__(self, x, y):
        """Constructor

        :param x: x-coordinate of the Point
        :type x: number

        :param y: y-coordinate of the Point
        :type y: number
        """
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        """string method -- for print function"""
        return "point({0}, {1})".format(self.x, self.y)

    def as_wkt(self):
        """Well Known Text of this point"""
        return "POINT({} {})".format(self.x, self.y)

    def distance(self, other):
        """Returns distance to the *other* point
        (assuming Euclidean geometry)

        :param other: the point to compute the distance to
        :type other: Point
        """
        return math.dist([self.x, self.y], [other.x, other.y])

    def __hash__(self):
        """Allows a Point instance to be used
        (as key) in a dictionary or in a set (i.e. hashed collections)."""
        return hash((self.x, self.y))

    def __eq__(self, other):
        """Compare Point instances for equivalence
        (this object instance == other instance?).

        :param other: the point to compare with
        :type other: Point

        Returns True/False
        """
        return self.x == other.x and self.y == other.y


class Circle:
    """Circle, with center and radius"""

    def __init__(self, center, radius):
        """Constructor

        :param center: center of the circle
        :type center: Point

        :param radius: radius of the circle
        :type radius: float
        """
        self.center = center
        self.radius = float(radius)

    def __str__(self):
        """string method -- for print function"""
        return "circle<c:{0}, r:{1}>".format(self.center, self.radius)

    def area(self):
        """Returns the area of the circle"""
        return math.pi * self.radius**2

    def perimeter(self):
        """Returns the perimeter of the circle"""
        return 2 * math.pi * self.radius

    def covers(self, pt):
        """Returns True when the circle covers point *pt*,
        False otherwise

        Note that we consider points that are near to the boundary of the
        circle also to be covered by the circle (arbitrary epsilon to use: 1e-8).
        """
        distance = math.sqrt((pt.x - self.center.x) ** 2 + (pt.y - self.center.y) ** 2)
        return distance <= self.radius + 1e-8

    def as_wkt(self):
        """Returns WKT str, discretizing the circle into straight
        line segments
        """
        N = 400  # the number of segments
        step = 2.0 * math.pi / N
        pts = []
        for i in range(N):
            pts.append(
                Point(
                    self.center.x + math.cos(i * step) * self.radius,
                    self.center.y + math.sin(i * step) * self.radius,
                )
            )
        pts.append(pts[0])
        coordinates = ["{0} {1}".format(pt.x, pt.y) for pt in pts]
        coordinates = ", ".join(coordinates)
        return "POLYGON(({0}))".format(coordinates)


class Triangle:
    def __init__(self, p0, p1, p2):
        """Constructor

        Arguments: p0, p1, p2 -- Point instances
        """
        self.p0, self.p1, self.p2 = p0, p1, p2

    def __str__(self):
        return "triangle<p0:{0}, p1:{1}, p2:{2}>".format(self.p0, self.p1, self.p2)

    def as_wkt(self):
        """String representation"""
        points = [
            "{0.x} {0.y}".format(pt) for pt in (self.p0, self.p1, self.p2, self.p0)
        ]
        return "POLYGON(({0}))".format(", ".join(points))

    def circumcircle(self):
        """Returns Circle instance that intersects the 3 points of the triangle.

        Note, the assignment sheet contains a formula for calculating the
        center of this Circle.
        """
        ax, ay = self.p0.x, self.p0.y
        bx, by = self.p1.x, self.p1.y
        cx, cy = self.p2.x, self.p2.y
        d = 2.0 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        if d == 0:
            return None  # TODO: fix here
        ux = (
            (ax**2 + ay**2) * (by - cy)
            + (bx**2 + by**2) * (cy - ay)
            + (cx**2 + cy**2) * (ay - by)
        ) / d
        uy = (
            (ax**2 + ay**2) * (cx - bx)
            + (bx**2 + by**2) * (ax - cx)
            + (cx**2 + cy**2) * (bx - ax)
        ) / d
        center = Point(ux, uy)
        radius = center.distance(self.p0)
        return Circle(center, radius)

    def area(self):
        """Area of this triangle, using Heron's formula.

        In case you run into a negative value for taking the square root
        (which is not possible), and one of the terms is very close to zero,
        it is okay to return 0.0 for the area.
        """
        node_0_1 = self.p0.distance(self.p1)
        node_1_2 = self.p1.distance(self.p2)
        node_2_0 = self.p2.distance(self.p0)
        s = self.perimeter() / 2
        area = math.sqrt(s * (s - node_0_1) * (s - node_1_2) * (s - node_2_0))
        if isinstance(area, complex):
            area = 0.0
        return area

    def perimeter(self):
        """Perimeter of this triangle (float)"""
        return (
            self.p0.distance(self.p1)
            + self.p1.distance(self.p2)
            + self.p2.distance(self.p0)
        )

    def covers(self, pt):
        """Returns True when the triangle covers point *pt*, False otherwise

        The implementation of this method should use the fact that a triangle
        covers a point, iff the summed area of the 3 triangles
        formed by (pt0, pt1, pt) and (pt1, pt2, pt) and (pt2, pt0, pt)
        is approximately equal (arbitrary epsilon to use: 1e-8) to the area
        of this triangle formed by its points (pt0, pt1, pt2).
        """
        self.area()
        tri1 = Triangle(self.p0, self.p1, pt)
        tri2 = Triangle(self.p1, self.p2, pt)
        tri3 = Triangle(self.p2, self.p0, pt)
        summed_area = tri1.area() + tri2.area() + tri3.area()
        if abs(summed_area - self.area()) < 1e-8:
            return True
        else:
            return False


def _test():
    # If you want, you can write tests in this function
    pass


if __name__ == "__main__":
    _test()
