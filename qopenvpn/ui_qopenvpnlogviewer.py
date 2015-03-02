# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qopenvpn/qopenvpnlogviewer.ui'
#
# Created: Mon Mar  2 00:32:39 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_QOpenVPNLogViewer(object):
    def setupUi(self, QOpenVPNLogViewer):
        QOpenVPNLogViewer.setObjectName(_fromUtf8("QOpenVPNLogViewer"))
        QOpenVPNLogViewer.resize(1000, 560)
        self.gridLayout = QtGui.QGridLayout(QOpenVPNLogViewer)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.logViewerEdit = QtGui.QPlainTextEdit(QOpenVPNLogViewer)
        self.logViewerEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.logViewerEdit.setObjectName(_fromUtf8("logViewerEdit"))
        self.gridLayout.addWidget(self.logViewerEdit, 0, 0, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(QOpenVPNLogViewer)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.ipAddressEdit = QtGui.QLineEdit(QOpenVPNLogViewer)
        self.ipAddressEdit.setReadOnly(True)
        self.ipAddressEdit.setObjectName(_fromUtf8("ipAddressEdit"))
        self.horizontalLayout.addWidget(self.ipAddressEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.refreshButton = QtGui.QPushButton(QOpenVPNLogViewer)
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.gridLayout.addWidget(self.refreshButton, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(453, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(QOpenVPNLogViewer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 1)

        self.retranslateUi(QOpenVPNLogViewer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QOpenVPNLogViewer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QOpenVPNLogViewer.reject)
        QtCore.QMetaObject.connectSlotsByName(QOpenVPNLogViewer)

    def retranslateUi(self, QOpenVPNLogViewer):
        QOpenVPNLogViewer.setWindowTitle(_translate("QOpenVPNLogViewer", "QOpenVPN Log Viewer", None))
        self.label.setText(_translate("QOpenVPNLogViewer", "IP address:", None))
        self.refreshButton.setText(_translate("QOpenVPNLogViewer", "Refresh", None))

