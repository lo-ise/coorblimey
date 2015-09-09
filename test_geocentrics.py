import unittest

from coorblimey.geocentrics import Geocentrics


class TestGeocentrics(unittest.TestCase):

    def test_grs80_to_geographic(self):
        geo1      = Geocentrics(1418595, -689557, -6159338)
        lat_long1 = geo1.make_geographic()
        self.assertEqual(lat_long1, [-75.72836167, -25.92366687, 30.705])

        geo2      = Geocentrics(1425925.3230, -703655.7929, -6156081.8741)
        lat_long2 = geo2.make_geographic()
        self.assertEqual(lat_long2, [-75.61017435, -26.26509986, 40.322])


    def test_user_input(self):
        geo_grs80 = Geocentrics(1418595, -689557, -6159338, ellipsoid='grs80')
        self.assertEqual('GRS80', geo_grs80.ellipsoid)

        geo_wgs84 = Geocentrics(1418595, -689557, -6159338, ellipsoid='wGS84')
        self.assertEqual('WGS84', geo_wgs84.ellipsoid)
        

    def test_wgs84_to_geographic(self):
        geo      = Geocentrics(1418595, -689557, -6159338, ellipsoid='WGS84')
        lat_long = geo.make_geographic()
        self.assertEqual(lat_long, [-75.72836167, -25.92366687, 30.705])


if __name__ == "__main__":
    unittest.main()
