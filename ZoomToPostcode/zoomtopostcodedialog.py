# -*- coding: utf-8 -*-
"""
/***************************************************************************
 zoomtopostcodedialog
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
"""

from PyQt4 import QtGui
from licence_dlg import Ui_ZoomToPostcode


class LicenceDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_ZoomToPostcode()
        self.ui.setupUi(self)
