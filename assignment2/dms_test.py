import unittest
from dms import format_dd_as_dms, dd_dms


class Testing(unittest.TestCase):
    def test_dms(self):
        self.assertEqual(dd_dms(0), (0, 0, 0))
        # TODO: fix test case later
        # self.assertEqual(dd_dms(1.40722), (1, 24, 26.0))
        # self.assertEqual(dd_dms(-1.40722), (-1, 24, 26.0))

    def test_format_dms(self):
        test_cases = [
            ((0.0, 0.0), "N   0°  0'  0.0000\", E   0°  0'  0.0000\""),
            ((52.0, 4.3287), "N  52°  0'  0.0000\", E   4° 19' 43.3200\""),
            ((-52.0, 4.3287), "S  52°  0'  0.0000\", E   4° 19' 43.3200\""),
            ((52.0, -4.3287), "N  52°  0'  0.0000\", W   4° 19' 43.3200\""),
            ((-52.0, -4.3287), "S  52°  0'  0.0000\", W   4° 19' 43.3200\""),
            ((45.0, 180.0), "N  45°  0'  0.0000\", E 180°  0'  0.0000\""),
            ((-45.0, -180.0), "S  45°  0'  0.0000\", W 180°  0'  0.0000\""),
            ((-50.4567, 4.3287), "S  50° 27' 24.1200\", E   4° 19' 43.3200\""),
        ]
        coordinates = (
            (0.0, 0.0),
            (52.0, 4.3287),
            (-52.0, 4.3287),
            (52.0, -4.3287),
            (-52.0, -4.3287),
            (45.0, 180.0),
            (-45.0, -180.0),
            (-50.4567, 4.3287),
        )
        for test_case in test_cases:
            self.assertEqual(format_dd_as_dms(test_case[0]), test_case[1])


if __name__ == "__main__":
    unittest.main()
