from tienstra import distance
import unittest


class Testing(unittest.TestCase):
    def test_abc(self):
        print("dist----", distance(1.0, 2.0, 3.0, 4.0))
        # self.assertEqual(distance(1.0, 2.0, 3.0, 4.0))


if __name__ == "__main__":
    unittest.main()
