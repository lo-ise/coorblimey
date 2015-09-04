import unittest
from geocentrics import Geocentrics

class TestGeocentrics(unittest.TestCase):

    def test_to_geographic(self):
        geo      = Geocentrics(1418595, -689557, -6159338)
        lat_long = geo.make_geographic()
        self.assertEqual(lat_long, [-75.7283616724, -25.9236668699, 30.705])


if __name__ == "__main__":
    unittest.main()

