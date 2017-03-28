# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qopenvpn/qopenvpnsettings.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QOpenVPNSettings(object):
    def setupUi(self, QOpenVPNSettings):
        QOpenVPNSettings.setObjectName("QOpenVPNSettings")
        QOpenVPNSettings.resize(300, 200)
        self.gridLayout = QtWidgets.QGridLayout(QOpenVPNSettings)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(QOpenVPNSettings)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.vpnNameComboBox = QtWidgets.QComboBox(QOpenVPNSettings)
        self.vpnNameComboBox.setObjectName("vpnNameComboBox")
        self.gridLayout.addWidget(self.vpnNameComboBox, 0, 1, 1, 2)
        self.warningCheckBox = QtWidgets.QCheckBox(QOpenVPNSettings)
        self.warningCheckBox.setObjectName("warningCheckBox")
        self.gridLayout.addWidget(self.warningCheckBox, 1, 0, 1, 3)
        self.line_2 = QtWidgets.QFrame(QOpenVPNSettings)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 3)
        self.sudoCheckBox = QtWidgets.QCheckBox(QOpenVPNSettings)
        self.sudoCheckBox.setObjectName("sudoCheckBox")
        self.gridLayout.addWidget(self.sudoCheckBox, 3, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(QOpenVPNSettings)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 2)
        self.sudoCommandEdit = QtWidgets.QLineEdit(QOpenVPNSettings)
        self.sudoCommandEdit.setObjectName("sudoCommandEdit")
        self.gridLayout.addWidget(self.sudoCommandEdit, 4, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(QOpenVPNSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 3)

        self.retranslateUi(QOpenVPNSettings)
        self.buttonBox.accepted.connect(QOpenVPNSettings.accept)
        self.buttonBox.rejected.connect(QOpenVPNSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(QOpenVPNSettings)
        QOpenVPNSettings.setTabOrder(self.vpnNameComboBox, self.warningCheckBox)
        QOpenVPNSettings.setTabOrder(self.warningCheckBox, self.sudoCheckBox)
        QOpenVPNSettings.setTabOrder(self.sudoCheckBox, self.sudoCommandEdit)
        QOpenVPNSettings.setTabOrder(self.sudoCommandEdit, self.buttonBox)

    def retranslateUi(self, QOpenVPNSettings):
        _translate = QtCore.QCoreApplication.translate
        QOpenVPNSettings.setWindowTitle(_translate("QOpenVPNSettings", "QOpenVPN Settings"))
        self.label.setText(_translate("QOpenVPNSettings", "VPN name:"))
        self.warningCheckBox.setText(_translate("QOpenVPNSettings", "Show warning when disconnected"))
        self.sudoCheckBox.setText(_translate("QOpenVPNSettings", "Use sudo"))
        self.label_2.setText(_translate("QOpenVPNSettings", "Sudo command:"))

