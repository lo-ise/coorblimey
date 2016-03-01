coorblimey
==========

.. image:: https://codeclimate.com/github/lo-ise/coorblimey/badges/gpa.svg 
   :target: https://codeclimate.com/github/lo-ise/coorblimey 
   :alt: Code Climate 
       
.. image:: https://circleci.com/gh/lo-ise/coorblimey.png?style=shield 
   :target: https://circleci.com/gh/lo-ise/coorblimey/tree/master 


What is it?
-----------

coorblimey is an open source Python3 library to transform geocentric
coordinates to geographic, and vice versa.

Formulas for the calculations have been taken from:

*Datums and Map Projections: For Remote Sensing, GIS and Surveying,
Second Edition, by Jonathan IIiffe (Editor), Roger Lott.*

Results were checked against `this handy
tool <http://www.apsalin.com/convert-cartesian-to-geodetic.aspx>`__.

In it's present state...
------------------------

... it only does the geocentric to geographic bit, and only has the
ability to do this with either GRS80 or WGS84 ellipsoids.

It outputs latitude, longitude and height above ellipsoid. The precision
of this for latitude and longitude is 10 decimal places. For height, to
the millimetre. 


Installation
------------

Easy hopefully, just...

::

    pip install coorblimey

 

Usage
-----

You can either use this as a command line tool, or you can import it
into your python programs...

**... as a command line tool**


::

    coorblimey -t to_geographic -x 1418595 -y -689557 -z -6159338 -e GRS80

This will give:

::

    Geographic coordinates (GRS80)
    lat: -75.7283616724, lon: -25.9236668699, h: 30.705


**... in Python programs**



.. code:: python

    from coorblimey.geocentrics import Geocentrics

    geo      = Geocentrics(1418595, -689557, -6159338, ellipsoid='GRS80')
    latlongs = geo.make_geographic()

``latlongs`` with be a list ``[lat, lon, z]``

