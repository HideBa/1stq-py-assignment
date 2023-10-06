import unittest
from transformer import as_timestamp_bitlist, as_dicts


class Testing(unittest.TestCase):
    def test_as_timestamp_bitlist(self):
        test_cases = [
            (
                [
                    (
                        "2017-07-21Z00:00:17.986965",
                        "33P>BD5P00PCLb<MeAEH??vR2Djr",
                        0,
                    ),
                    (
                        "2017-07-21Z00:00:21.103635",
                        "13aDpUwP000CMB<Me9J;Dgvb2<A;",
                        0,
                    ),
                ],
                [
                    (
                        "2017-07-21Z00:00:17.986965",
                        "00110011000010111100011001010000",
                    ),
                    (
                        "2017-07-21Z00:00:21.103635",
                        "00010011101011010011100001100000",
                    ),
                ],
            )
        ]
        for test_case in test_cases:
            self.assertEqual(as_timestamp_bitlist(test_case[0]), test_case[1])


if __name__ == "__main__":
    unittest.main()
