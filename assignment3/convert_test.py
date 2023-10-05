from convert import read_asc, marching_squares, write_segments, convert
import unittest


class Testing(unittest.TestCase):
    # def test_read_asc(self):
    #     (rows, cols, xll, yll, size, nodataval, data) = read_asc(
    #         "./assignment3/giraffe.asc"
    #     )
    #     self.assertEqual(rows, 242)
    #     self.assertEqual(cols, 208)
    #     self.assertEqual(xll, 0.0)
    #     self.assertEqual(yll, 0.0)
    #     self.assertEqual(size, 30.0)
    #     self.assertEqual(nodataval, -9999)
    #     self.assertEqual(len(data), 242)
    #     self.assertEqual(len(data[0]), 208)

    #     (rows, cols, xll, yll, size, nodataval, data) = read_asc(
    #         "./assignment3/holland.asc"
    #     )
    #     self.assertEqual(rows, 395)
    #     self.assertEqual(cols, 362)
    #     self.assertEqual(xll, 100.0)
    #     self.assertEqual(yll, 1000.0)
    #     self.assertEqual(size, 50.0)
    #     self.assertEqual(nodataval, -9999)
    #     self.assertEqual(len(data), 1)
    #     self.assertEqual(len(data[0]), 395 * 362)

    #     (rows, cols, xll, yll, size, nodataval, data) = read_asc(
    #         "./assignment3/simple_eol.asc"
    #     )
    #     self.assertEqual(rows, 2)
    #     self.assertEqual(cols, 1)
    #     self.assertEqual(xll, 1.0)
    #     self.assertEqual(yll, 20.0)
    #     self.assertEqual(size, 10.0)
    #     self.assertEqual(nodataval, -9999)
    #     self.assertEqual(len(data), 2)
    #     self.assertEqual(len(data[0]), 1)

    #     print("read_asc test passed")

    def test_marching_squares(self):
        data = read_asc("./assignment3/giraffe.asc")
        res = marching_squares(*data)
        # self.assertEqual(rows, 242)

        print("marching_squares test passed")


if __name__ == "__main__":
    unittest.main()
