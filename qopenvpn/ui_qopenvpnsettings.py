# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qopenvpn/qopenvpnsettings.ui'
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

class Ui_QOpenVPNSettings(object):
    def setupUi(self, QOpenVPNSettings):
        QOpenVPNSettings.setObjectName(_fromUtf8("QOpenVPNSettings"))
        QOpenVPNSettings.resize(300, 200)
        self.gridLayout = QtGui.QGridLayout(QOpenVPNSettings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(QOpenVPNSettings)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.vpnNameComboBox = QtGui.QComboBox(QOpenVPNSettings)
        self.vpnNameComboBox.setObjectName(_fromUtf8("vpnNameComboBox"))
        self.gridLayout.addWidget(self.vpnNameComboBox, 0, 1, 1, 2)
        self.warningCheckBox = QtGui.QCheckBox(QOpenVPNSettings)
        self.warningCheckBox.setObjectName(_fromUtf8("warningCheckBox"))
        self.gridLayout.addWidget(self.warningCheckBox, 1, 0, 1, 3)
        self.line_2 = QtGui.QFrame(QOpenVPNSettings)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 3)
        self.sudoCheckBox = QtGui.QCheckBox(QOpenVPNSettings)
        self.sudoCheckBox.setObjectName(_fromUtf8("sudoCheckBox"))
        self.gridLayout.addWidget(self.sudoCheckBox, 3, 0, 1, 2)
        self.label_2 = QtGui.QLabel(QOpenVPNSettings)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 2)
        self.sudoCommandEdit = QtGui.QLineEdit(QOpenVPNSettings)
        self.sudoCommandEdit.setObjectName(_fromUtf8("sudoCommandEdit"))
        self.gridLayout.addWidget(self.sudoCommandEdit, 4, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(QOpenVPNSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 3)

        self.retranslateUi(QOpenVPNSettings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QOpenVPNSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QOpenVPNSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(QOpenVPNSettings)
        QOpenVPNSettings.setTabOrder(self.vpnNameComboBox, self.warningCheckBox)
        QOpenVPNSettings.setTabOrder(self.warningCheckBox, self.sudoCheckBox)
        QOpenVPNSettings.setTabOrder(self.sudoCheckBox, self.sudoCommandEdit)
        QOpenVPNSettings.setTabOrder(self.sudoCommandEdit, self.buttonBox)

    def retranslateUi(self, QOpenVPNSettings):
        QOpenVPNSettings.setWindowTitle(_translate("QOpenVPNSettings", "QOpenVPN Settings", None))
        self.label.setText(_translate("QOpenVPNSettings", "VPN name:", None))
        self.warningCheckBox.setText(_translate("QOpenVPNSettings", "Show warning when disconnected", None))
        self.sudoCheckBox.setText(_translate("QOpenVPNSettings", "Use sudo", None))
        self.label_2.setText(_translate("QOpenVPNSettings", "Sudo command:", None))

