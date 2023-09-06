from solve import abc
import unittest


class Testing(unittest.TestCase):
    def test_abc(self):
        self.assertEqual(abc(2.0, 0.0, 0.0), (0.0))
        self.assertEqual(abc(1.0, 3.0, 2.0), (-1.0, -2.0))
        self.assertEqual(abc(3.0, 4.5, 9.0), "not real")


if __name__ == "__main__":
    unittest.main()
