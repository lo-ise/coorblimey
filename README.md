# coorblimey

[![Code Climate](https://codeclimate.com/github/lo-ise/coorblimey/badges/gpa.svg)](https://codeclimate.com/github/lo-ise/coorblimey)

[![circleci](https://circleci.com/gh/lo-ise/coorblimey.png?style=shield)](https://circleci.com/gh/lo-ise/coorblimey)

## What is it?

coorblimey is an open source Python3 library to transform geocentric coordinates to geographic, and vice versa. 

Formulas for the calculations have been taken from:

_Datums and Map Projections: For Remote Sensing, GIS and Surveying, Second Edition, by Jonathan IIiffe (Editor), Roger Lott._

Results were checked against [this handy tool](http://www.apsalin.com/convert-cartesian-to-geodetic.aspx). 


## In it's present state...

... it only does the geocentric to geographic bit, and only has the ability to do this with either GRS80 or WGS84 ellipsoids.

It outputs latitude, longitude and height above ellipsoid. The precision of this for latitude and longitude is 10 decimal places. For height, to the millimetre. 

