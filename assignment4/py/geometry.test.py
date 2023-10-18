import math
import unittest
from geometry import Point, Circle, Triangle


class TestPoint(unittest.TestCase):
    def test_init(self):
        p = Point(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_str(self):
        p = Point(1, 2)
        self.assertEqual(str(p), "(1, 2)")

    def test_as_wkt(self):
        p = Point(1, 2)
        self.assertEqual(p.as_wkt(), "POINT(1 2)")

    def test_distance(self):
        p1 = Point(1, 2)
        p2 = Point(4, 6)
        self.assertEqual(p1.distance(p2), math.sqrt(18))


class TestCircle(unittest.TestCase):
    def test_init(self):
        p = Point(1, 2)
        c = Circle(p, 3)
        self.assertEqual(c.center, p)
        self.assertEqual(c.radius, 3)

    def test_str(self):
        p = Point(1, 2)
        c = Circle(p, 3)
        self.assertEqual(str(c), "circle<c:(1, 2), r:3.0>")

    def test_area(self):
        p = Point(1, 2)
        c = Circle(p, 3)
        self.assertAlmostEqual(c.area(), math.pi * 9)

    def test_perimeter(self):
        p = Point(1, 2)
        c = Circle(p, 3)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 3)

    def test_covers(self):
        p = Point(1, 2)
        c = Circle(p, 3)
        self.assertTrue(c.covers(Point(2, 3)))
        self.assertTrue(c.covers(Point(1, 5)))
        self.assertTrue(c.covers(Point(4, 2)))
        self.assertTrue(c.covers(Point(1, 2)))
        self.assertFalse(c.covers(Point(5, 5)))
        self.assertFalse(c.covers(Point(0, 0)))


class TestTriangle(unittest.TestCase):
    def test_init(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(5, 6)
        t = Triangle(p1, p2, p3)
        self.assertEqual(t.p0, p1)
        self.assertEqual(t.p1, p2)
        self.assertEqual(t.p2, p3)

    def test_str(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(5, 6)
        t = Triangle(p1, p2, p3)
        self.assertEqual(str(t), "triangle<(1, 2), (3, 4), (5, 6)>")
