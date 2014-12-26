# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_zoomtopostcode.ui'
#
# Created: Fri Oct 11 16:19:39 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ZoomToPostcode(object):
    def setupUi(self, ZoomToPostcode):
        ZoomToPostcode.setObjectName(_fromUtf8("ZoomToPostcode"))
        ZoomToPostcode.resize(424, 168)
        self.buttonBox = QtGui.QDialogButtonBox(ZoomToPostcode)
        self.buttonBox.setGeometry(QtCore.QRect(300, 10, 111, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget_2 = QtGui.QWidget(ZoomToPostcode)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 20, 261, 33))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.tog = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.tog.setSpacing(6)
        self.tog.setMargin(0)
        self.tog.setObjectName(_fromUtf8("tog"))
        self.label_7 = QtGui.QLabel(self.layoutWidget_2)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tog.addWidget(self.label_7)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.tog.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(ZoomToPostcode)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 371, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(ZoomToPostcode)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ZoomToPostcode.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ZoomToPostcode.reject)
        QtCore.QMetaObject.connectSlotsByName(ZoomToPostcode)

    def retranslateUi(self, ZoomToPostcode):
        ZoomToPostcode.setWindowTitle(_translate("ZoomToPostcode", "Zoom to Postcode", None))
        self.label_7.setText(_translate("ZoomToPostcode", "Enter a UK postcode", None))
        self.label_2.setText(_translate("ZoomToPostcode", "<html><head/><body><p><span style=\" font-size:7pt;\"> Contains Ordnance Survey data (C) Crown copyright and database right 2013</span></p><p><span style=\" font-size:7pt;\"> Contains Royal Mail data (C) Royal Mail copyright and database right 2013</span></p><p><span style=\" font-size:7pt;\"> Contains National Statistics data (C) Crown copyright and database right 2013</span></p></body></html>", None))

