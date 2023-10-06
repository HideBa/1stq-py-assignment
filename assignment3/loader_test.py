import unittest
from loader import get_payload, read_payloads


class Testing(unittest.TestCase):
    def test_get_payload(self):
        test_cases = [
            (
                "2017-07-21Z00:00:17.986965	!AIVDM,1,1,,A,33P>BD5P00PCLb<MeAEH??vR2Djr,0*04",
                ("33P>BD5P00PCLb<MeAEH??vR2Djr", 0),
            ),
            (
                "2017-07-21Z00:00:21.103635	!AIVDM,1,1,,B,13aDpUwP000CMB<Me9J;Dgvb2<A;,0*63",
                ("13aDpUwP000CMB<Me9J;Dgvb2<A;", 0),
            ),
        ]
        for test_case in test_cases:
            self.assertEqual(get_payload(test_case[0]), test_case[1])

    def test_read_payloads(self):
        result = read_payloads("./assignment3/aislog.txt")
        self.assertEqual(
            result[0],
            (
                "2017-07-21Z00:00:17.986965",
                "33P>BD5P00PCLb<MeAEH??vR2Djr",
                0,
            ),
        )
        self.assertEqual(
            result[1],
            (
                "2017-07-21Z00:00:21.103635",
                "13aDpUwP000CMB<Me9J;Dgvb2<A;",
                0,
            ),
        )


if __name__ == "__main__":
    unittest.main()
