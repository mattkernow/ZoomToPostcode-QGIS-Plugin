# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_zoomtopostcode.ui'
#
# Created: Fri Dec 26 13:55:44 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_ZoomToPostcode(object):
    def setupUi(self, ZoomToPostcode):
        ZoomToPostcode.setObjectName(_fromUtf8("ZoomToPostcode"))
        ZoomToPostcode.resize(379, 122)
        self.gridLayout = QtWidgets.QGridLayout(ZoomToPostcode)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(ZoomToPostcode)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)

        self.retranslateUi(ZoomToPostcode)
        QtCore.QMetaObject.connectSlotsByName(ZoomToPostcode)

    def retranslateUi(self, ZoomToPostcode):
        ZoomToPostcode.setWindowTitle(_translate("ZoomToPostcode", "OS Licence", None))
        self.label_2.setText(_translate("ZoomToPostcode", "<html><head/><body><p><span style=\" font-size:7pt;\">Contains Ordnance Survey data (C) Crown copyright and database right 2015</span></p><p><span style=\" font-size:7pt;\">Contains Royal Mail data (C) Royal Mail copyright and database right 2015</span></p><p><span style=\" font-size:7pt;\">Contains National Statistics data (C) Crown copyright and database right 2015</span></p></body></html>", None))

