# coorblimey

## What is it?

coorblimey is an open source Python3 library to transform geocentric coordinates to geographic, and vice versa. 

Formulas for the calculations have been taken from:

Datums and Map Projections: For Remote Sensing, GIS and Surveying, Second Edition, by Jonathan IIiffe (Editor), Roger Lott.

Results can be checked [here](http://www.apsalin.com/convert-cartesian-to-geodetic.aspx). 


## In it's present state...

... it only does the geocentric to geographic bit, and only has the ability to do this with either GRS80 or WGS84 ellipsoids. 

## Useage

You can either use this as a command line tool, or as a module to import into your Python programs. 

### As a command line tool...

    coorblimey.py -t to_geographic -x 654321 -y 765433 -z 98765432

This will print the results. 

### As a module to import...

    from  coorblimey import Geocentrics
    
    geo = Geocentrics(654321, 765433, 98765432, ellipsoid='GRS80')
    geo.make_geographic()

