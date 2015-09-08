from __future__ import print_function
import argparse

from coorblimey.geocentrics import Geocentrics


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', type=str, metavar='transform', dest='transform', required=True,
                    choices=['to_geographic', 'to_geocentric'],
                    help='Select either to_geographic, or to_geocentric.')

    parser.add_argument('-x', type=float, metavar='x', dest='x', required=True, 
                    help='Enter x coordinate. If Geocentric this should be in metres. If Geographic, this should be in decimal degrees')

    parser.add_argument('-y', type=float, metavar='y', dest='y', required=True, 
                    help='Enter y coordinate. If Geocentric this should be in metres. If Geographic, this should be in decimal degrees')

    parser.add_argument('-z', type=float, metavar='z', dest='z', required=True, 
                    help='Enter z coordinate in metres.')

    parser.add_argument('-e', type=str, metavar='ellipsoid', dest='ellipsoid', required=True,
                    choices=['GRS80', 'WGS84'],
                    help='Select which ellipsoid your coordinates are in reference to. At the moment we only support either WGS84 or GRS80.')

    args = parser.parse_args()

    transform = args.transform
    ellipsoid = args.ellipsoid
    x         = args.x
    y         = args.y
    z         = args.z

    if transform == 'to_geographic':
        geo = Geocentrics(x, y, z, ellipsoid=ellipsoid)
        latlongs = geo.make_geographic()
        print("Geographic coordinates ({})".format(ellipsoid))
        print("lat: {0}, lon: {1}, h: {2}".format(latlongs[0], latlongs[1], latlongs[2]))
    elif transform == 'to_geocentric':
        print("coorblimey isn't this clever ... yet.")


if __name__ == "__main__":
    main()
