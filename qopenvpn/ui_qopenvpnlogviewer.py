# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qopenvpn/qopenvpnlogviewer.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QOpenVPNLogViewer(object):
    def setupUi(self, QOpenVPNLogViewer):
        QOpenVPNLogViewer.setObjectName("QOpenVPNLogViewer")
        QOpenVPNLogViewer.resize(1000, 560)
        self.gridLayout = QtWidgets.QGridLayout(QOpenVPNLogViewer)
        self.gridLayout.setObjectName("gridLayout")
        self.logViewerEdit = QtWidgets.QPlainTextEdit(QOpenVPNLogViewer)
        self.logViewerEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.logViewerEdit.setObjectName("logViewerEdit")
        self.gridLayout.addWidget(self.logViewerEdit, 0, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(QOpenVPNLogViewer)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ipAddressEdit = QtWidgets.QLineEdit(QOpenVPNLogViewer)
        self.ipAddressEdit.setReadOnly(True)
        self.ipAddressEdit.setObjectName("ipAddressEdit")
        self.horizontalLayout.addWidget(self.ipAddressEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.refreshButton = QtWidgets.QPushButton(QOpenVPNLogViewer)
        self.refreshButton.setObjectName("refreshButton")
        self.gridLayout.addWidget(self.refreshButton, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(453, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(QOpenVPNLogViewer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 1)

        self.retranslateUi(QOpenVPNLogViewer)
        self.buttonBox.accepted.connect(QOpenVPNLogViewer.accept)
        self.buttonBox.rejected.connect(QOpenVPNLogViewer.reject)
        QtCore.QMetaObject.connectSlotsByName(QOpenVPNLogViewer)

    def retranslateUi(self, QOpenVPNLogViewer):
        _translate = QtCore.QCoreApplication.translate
        QOpenVPNLogViewer.setWindowTitle(_translate("QOpenVPNLogViewer", "QOpenVPN Log Viewer"))
        self.label.setText(_translate("QOpenVPNLogViewer", "IP address:"))
        self.refreshButton.setText(_translate("QOpenVPNLogViewer", "Refresh"))

