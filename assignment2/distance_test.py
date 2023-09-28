import unittest
from distance import haversin


class Testing(unittest.TestCase):
    def test_haversin(self):
        # Test case 1: Same coordinates should result in a distance of 0
        latlon1 = (39.9496, -75.1503)  # Berlin coordinates
        distance = haversin(latlon1, latlon1)
        self.assertEqual(
            distance, 0.0, f"Expected distance: 0.0, Actual distance: {distance}"
        )

        # Test case 2: Different coordinates should result in a non-zero distance
        latlon2 = (38.8976, -77.0366)  # Paris coordinates
        distance = haversin(latlon1, latlon2)
        print("distance: ", round(distance, 2))
        self.assertEqual(
            round(distance, 2),
            199.83,
            f"Expected non-zero distance, Actual distance: {distance}",
        )

        # Test case 3: Distance between same coordinates but reverse order should be the same
        distance1 = haversin(latlon1, latlon2)
        distance2 = haversin(latlon2, latlon1)
        self.assertEqual(
            distance1,
            distance2,
            f"Distances are not equal: {distance1}, {distance2}",
        )


if __name__ == "__main__":
    unittest.main()
