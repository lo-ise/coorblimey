from __future__ import division
import math


class Geocentrics():
    
    def __init__(self, x, y, z, ellipsoid='GRS80'):
        """
        Input the x, y, z geocentric coordinates in metres.  
        
        """
        
        self.x = x
        self.y = y
        self.z = z
        self.ellipsoid = ellipsoid.upper()
        if self.ellipsoid == 'GRS80':
            self.a = 6378137.0
            self.b = 6356752.314140
        if self.ellipsoid == 'WGS84':
            self.a = 6378137.0
            self.b = 6356752.3142


    def __str__(self):
        """
        Printing the class gives a list back of the geocentric 
        coordinates that were input when class instantiated

        """

        output_text = """
        Geocentric Coordinates - {0} ellipsoid
        X = {1}
        Y = {2}
        Z = {3}
            """.format(self.ellipsoid, self.x, self.y, self.z)
        
        return output_text
        

    def make_geographic(self):
        """
        Outputs [lat,long,height] as a list. 
        Also calculates all other terms required. 

        """
       
        #p
        p = (self.x**2 + self.y**2)**0.5

        #u
        tan_u = self.z/p * self.a/self.b
        u_rad = math.atan(tan_u)
        u     = math.degrees(u_rad)

        #eccentricity, e
        e_sqrd = (self.a**2 - self.b**2)/self.a**2
        e      = math.sqrt(e_sqrd)

        #weird e symbol
        weirde = e_sqrd/(1-e_sqrd)

        #latitude
        tan_lat = (self.z + weirde * self.b * math.sin(u_rad)**3) \
                   /(p - e_sqrd * self.a * math.cos(u_rad)**3)
        lat_rad = math.atan(tan_lat)
        lat_deg = math.degrees(lat_rad)

        #v 
        v = self.a / ((1 - e_sqrd * math.sin(lat_rad)**2)**0.5)


        #long
        lon_rad = math.atan2(self.y, self.x)
        lon_deg = math.degrees(lon_rad)


        #height, h
        h = p * (1 / math.cos(lat_rad)) - v

        return [round(lat_deg, 8), round(lon_deg, 8), round(h, 3)]



