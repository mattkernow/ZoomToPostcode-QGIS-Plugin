# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ZoomToPostcode
                                 A QGIS plugin
 Zoom the map extent to any UK postcode
                             -------------------
        begin                : 2013-06-16
        copyright            : (C) 2015 by Matthew Walsh
        email                : walsh.gis@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Zoom to Postcode"


def description():
    return "Zoom the map extent to any UK postcode"


def version():
    return "Version 0.5"


def icon():
    return "zoomicon.png"


def qgisMinimumVersion():
    return "2.0"

def author():
    return "Matthew Walsh"

def email():
    return "walsh.gis@gmail.com"

def classFactory(iface):
    # load ZoomToPostcode class from file ZoomToPostcode
    from zoomtopostcode import ZoomToPostcode
    return ZoomToPostcode(iface)
