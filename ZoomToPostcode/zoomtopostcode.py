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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from zoomtopostcodedialog import LicenceDialog
import os.path
import pickle
import urllib2
import zipfile
import tempfile
import datetime
import xml.etree.ElementTree as ET


class ZoomToPostcode:

    def __init__(self, iface):
        # Save reference to the QGIS interface + canvas
        self.iface = iface
        self.canvas = iface.mapCanvas()
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'zoomtopostcode_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create licence dlg
        self.licence_dlg = LicenceDialog()

        # Create various class references
        self.marker = None
        self.completer = None
        self.previous_searches = []

    def initGui(self):
        # Create toolbar
        self.toolbar = self.iface.addToolBar("Zoom To Postcode Toolbar")
        self.toolbar.setObjectName("Zoom To Postcode Toolbar")
        self.toolbar_search = QLineEdit()
        self.toolbar_search.setMaximumWidth(100)
        self.toolbar_search.setAlignment(Qt.AlignLeft)
        self.toolbar_search.setPlaceholderText("Enter postcode...")
        self.toolbar.addWidget(self.toolbar_search)
        self.toolbar_search.returnPressed.connect(self.check_pkl)
        self.search_btn = QAction(QIcon(":/plugins/zoomtopostcode/zoomicon.png"), "Search",  self.iface.mainWindow())
        QObject.connect(self.search_btn, SIGNAL("triggered()"), self.check_pkl)
        self.toolbar.addActions([self.search_btn])

        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/zoomtopostcode/zoomicon.png"), u"Zoom to Postcode", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.toolbar.show)

        self.licence = QAction(u"OS Licence", self.iface.mainWindow())
        # connect the action to the run method
        self.licence.triggered.connect(self.licence_dlg.show)

        # Add toolbar button and menu item
        self.iface.addPluginToMenu(u"&Zoom to Postcode", self.action)
        self.iface.addPluginToMenu(u"&Zoom to Postcode", self.licence)

    def unload(self):
        # Remove the plugin menu item and toolbar
        self.iface.removePluginMenu(u"&Zoom to Postcode", self.action)
        self.iface.removePluginMenu(u"&Zoom to Postcode", self.licence)
        del self.toolbar

    def search_completer(self):
        self.completer = QCompleter(self.previous_searches, self.iface.mainWindow())
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

    def check_crs(self):
        # Check if a transformation needs to take place
        map_renderer = self.canvas.mapRenderer()
        srs = map_renderer.destinationCrs()
        current_crs = srs.authid()
        return current_crs

    def transform(self, cor):
        # Transforms point from british nation grid to map crs
        map_renderer = self.canvas.mapRenderer()
        srs = map_renderer.destinationCrs()
        crs_src = QgsCoordinateReferenceSystem(27700)
        crs_dest = QgsCoordinateReferenceSystem(srs)
        xform = QgsCoordinateTransform(crs_src, crs_dest)
        x = int(cor[0])
        y = int(cor[1])
        t_point = xform.transform(QgsPoint(x, y))
        return t_point

    def check_pkl(self):
        # Check the Pickle postcode dir exists
        checkpkl = os.path.isdir(os.path.join(self.plugin_dir, 'UK_Postcodes'))
        if checkpkl:
            xml_path = os.path.join(self.plugin_dir, r'UK_Postcodes/metadata.xml')
            check_xml = os.path.isfile(xml_path)
            if check_xml:
                check_currency = self.check_pcode_date(xml_path)
                if check_currency:
                    self.postcode_dict()
                else:
                    self.update_pcode_option()
            else:
                self.update_pcode_option()
        else:
            msg = "Postcode files must be downloaded to use this plugin, do you wish to continue?"
            goahead = QMessageBox.question(self.iface.mainWindow(), "Download Message", msg, QMessageBox.Yes, QMessageBox.No)
            if goahead == QMessageBox.Yes:
                self.download_pkl()
            else:
                pass

    def check_pcode_date(self, xml_path):
        # Parses metadata xml to check currency of pcodes
        url = "http://qgis.locationcentre.co.uk/ZoomToPostcode_medata.xml"
        request = urllib2.Request(url)
        u = urllib2.urlopen(request)
        tree_web = ET.parse(u)
        root_web = tree_web.getroot()
        current_version = ""
        for child in root_web:
            if child.tag == "pcode_date":
                current_version = child.text
        tree_plugin = ET.parse(xml_path)
        root_plugin = tree_plugin.getroot()
        last_update = ""
        for child in root_plugin:
            if child.tag == "pcode_date":
                last_update = child.text
        last_up_datetime = datetime.datetime.strptime(last_update, '%Y-%m-%d')
        curr_ver_datetime = datetime.datetime.strptime(current_version, '%Y-%m-%d')
        if last_up_datetime.date() >= curr_ver_datetime.date():
            return True  # Return True for up-to-date pcodes
        else:
            return False  # False requires download to update

    def update_pcode_option(self):
        # Provide option to update postcodes
        msg = "Updated postcode files are available, do you wish to download?"
        goahead = QMessageBox.question(self.iface.mainWindow(), "Download Message", msg, QMessageBox.Yes, QMessageBox.No)
        if goahead == QMessageBox.Yes:
            self.download_pkl()
        if goahead == QMessageBox.No:
            self.postcode_dict()

    def download_pkl(self):
        # Download the Pickle postcode file to the plugin dir
        pcode_path = os.path.join(os.path.dirname(__file__), 'UK_Postcodes')
        if not os.path.exists(pcode_path):
            os.makedirs(pcode_path)
        url = "http://qgis.locationcentre.co.uk/UK_Postcodes.zip"
        os.umask(0002)
        try:
            req = urllib2.urlopen(url)
            total_size = int(req.info().getheader('Content-Length').strip())
            downloaded = 0
            CHUNK = 256 * 10240
            dlbar = QProgressBar()
            dlbar.setMinimum(0)
            dlbar.setMaximum(total_size)
            zip_temp = tempfile.NamedTemporaryFile(mode='w+b', suffix='.zip', delete=False)
            zip_temp_n = zip_temp.name
            zip_temp.seek(0)
            with open(zip_temp_n, 'wb') as fp:
                while True:
                    dlbar.show()
                    chunk = req.read(CHUNK)
                    downloaded += len(chunk)
                    dlbar.setValue(downloaded)
                    if not chunk:
                        break
                    fp.write(chunk)
        except urllib2.HTTPError, e:
            QMessageBox.information(self.iface.mainWindow(), "HTTP Error", "Unable to download file")
        pcode_zip = zipfile.ZipFile(zip_temp)
        pcode_zip.extractall(pcode_path)
        zip_temp.close()
        self.check_pkl()

    def postcode_dict(self):
        # Create dictionary of postcodes from correct Pickle file
        try:
            input_pcode = self.toolbar_search.text().replace(' ', '')
            if input_pcode[1].isdigit():
                find_pkl = str(r"UK_Postcodes/" + input_pcode[:1] + ".pkl")
            else:
                find_pkl = str(r"UK_Postcodes/" + input_pcode[:2] + ".pkl")
            pklfile = open(os.path.join(os.path.dirname(__file__), find_pkl), 'rb')
            pcode_dict = pickle.load(pklfile)
            pklfile.close()
            if input_pcode.upper() not in self.previous_searches:
                self.previous_searches.append(input_pcode.upper())
                self.search_completer()
                self.toolbar_search.setCompleter(self.completer)
            self.zoomto(pcode_dict)
        except (KeyError, IOError):
            QMessageBox.information(self.iface.mainWindow(), "Invalid postcode", "The postcode you entered was not found")
        except IndexError:
            pass

    def zoomto(self, pcode_dict):
        # Find the coordinates for postcode in the dictionary
        current_crs = self.check_crs()
        input_pc = self.toolbar_search.text()
        input_pc_fmt = str(input_pc).replace(' ', '').upper()
        find = pcode_dict[input_pc_fmt]
        x = find[0]
        y = find[1]
        if current_crs != "EPSG:27700":
            cor = (x, y)
            point = self.transform(cor)
            self.update_canvas(point)
        else:
            point = (x, y)
            self.update_canvas(point)

    def update_canvas(self, point):
        # Update the canvas and add vertex marker
        x = point[0]
        y = point[1]
        scale = 120
        rect = QgsRectangle(float(x)-scale, float(y)-scale, float(x)+scale, float(y)+scale)
        self.canvas.setExtent(rect)
        self.marker = QgsVertexMarker(self.canvas)
        self.marker.setIconSize(15)
        self.marker.setPenWidth(2)
        self.marker.setCenter(QgsPoint(int(x), int(y)))
        self.canvas.refresh()
        self.canvas.extentsChanged.connect(self.remove_marker)

    def remove_marker(self):
        # Remove vertex marker
        self.marker.hide()
        self.canvas.scene().removeItem(self.marker)
        self.canvas.extentsChanged.disconnect(self.remove_marker)
