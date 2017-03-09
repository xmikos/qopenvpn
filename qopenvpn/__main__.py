#!/usr/bin/env python

import sys, os, subprocess, socket, glob, signal
from PyQt4 import QtCore, QtGui

from qopenvpn import stun
from qopenvpn.ui_qopenvpnsettings import Ui_QOpenVPNSettings
from qopenvpn.ui_qopenvpnlogviewer import Ui_QOpenVPNLogViewer


# Allow CTRL+C and/or SIGTERM to kill us (PyQt blocks it otherwise)
signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.signal(signal.SIGTERM, signal.SIG_DFL)


class QOpenVPNSettings(QtGui.QDialog, Ui_QOpenVPNSettings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        settings = QtCore.QSettings()
        self.sudoCommandEdit.setText(settings.value("sudo_command") or "kdesu")
        self.sudoCheckBox.setChecked(settings.value("use_sudo", False, type=bool))
        self.warningCheckBox.setChecked(settings.value("show_warning", False, type=bool))


        # Checks for the new location of OpenVPN configuration files introduced in OpenVPN 2.4
        # See https://github.com/OpenVPN/openvpn/blob/master/Changes.rst#user-visible-changes
        # "The configuration files are picked up from the /etc/openvpn/server/ and /etc/openvpn/client/ directories (depending on unit file)."
        # Remove this unaesthetic version check when openvpn 2.4 is widely accepcted

        output, _ = subprocess.Popen(["/usr/bin/env", "openvpn", "--version"], stdout=subprocess.PIPE).communicate()

        # Take second tuple of version output (i.e. `2.4.0`)
        # and extract its major and minor components (i.e. 2 and 4)
        versionString = output.decode("utf8").split()[1]
        versionComponents = versionString.split(".")

        if len(versionComponents) >= 2:
            major, minor = versionComponents[0:2]

            major = int(major)
            minor = int(minor)

        else:
            print("Couldn't determine the installed OpenVPN version, assuming v0.0", file=sys.stderr)
            major = minor = 0

        # Matches version 2.4.x or greater
        if major >= 2 and minor >= 4:
            settings.setValue("config_location", "/etc/openvpn/client/*.conf")
            settings.setValue("service_name", "openvpn-client")
        else:
            settings.setValue("config_location", "/etc/openvpn/*.conf")
            settings.setValue("service_name", "openvpn")


        # Fill VPN combo box with .conf files from /etc/openvpn{,/client}
        for f in sorted(glob.glob(settings.value("config_location"))):
            vpn_name = os.path.splitext(os.path.basename(f))[0]
            self.vpnNameComboBox.addItem(vpn_name)

        i = self.vpnNameComboBox.findText(settings.value("vpn_name"))
        if i > -1:
            self.vpnNameComboBox.setCurrentIndex(i)

    def accept(self):
        settings = QtCore.QSettings()
        settings.setValue("sudo_command", self.sudoCommandEdit.text())
        settings.setValue("use_sudo", self.sudoCheckBox.isChecked())
        settings.setValue("show_warning", self.warningCheckBox.isChecked())
        settings.setValue("vpn_name", self.vpnNameComboBox.currentText())
        QtGui.QDialog.accept(self)


class QOpenVPNLogViewer(QtGui.QDialog, Ui_QOpenVPNLogViewer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.refreshButton.clicked.connect(self.refresh)
        self.refresh()

    def journalctl(self, disable_sudo=False):
        """Run journalctl command and get OpenVPN logs"""
        settings = QtCore.QSettings()
        cmdline = []
        if not disable_sudo and settings.value("use_sudo", type=bool):
            cmdline.append(settings.value("sudo_command") or "sudo")
        cmdline.extend(["journalctl", "-b", "-u", "{}@{}".format(settings.value("service_name"), settings.value("vpn_name"))])
        try:
            output = subprocess.check_output(cmdline)
        except subprocess.CalledProcessError as e:
            output = e.output
        return output

    def getip(self):
        """Get external IP address and hostname"""
        try:
            stunclient = stun.StunClient()
            ip, port = stunclient.get_ip()
        except:
            ip = ""

        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = ""

        return (ip, hostname)

    def refresh(self):
        """Refresh logs"""
        self.logViewerEdit.setPlainText(self.journalctl(disable_sudo=True).decode("utf-8"))
        QtCore.QTimer.singleShot(0, self.refresh_timeout)

    def refresh_timeout(self):
        """Move scrollbar to bottom and refresh IP address
        (must be called by single shot timer or else scrollbar sometimes doesn't move)"""
        self.logViewerEdit.verticalScrollBar().setValue(self.logViewerEdit.verticalScrollBar().maximum())

        ip = self.getip()
        self.ipAddressEdit.setText("{} ({})".format(ip[0], ip[1]) if ip[1] else ip[0])


class QOpenVPNWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vpn_enabled = False

        self.create_actions()
        self.create_menu()
        self.create_icon()
        self.update_status()

        # Update status every 10 seconds
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_status)
        self.timer.start(5000)

        # Setup system tray icon doubleclick timer
        self.icon_doubleclick_timer = QtCore.QTimer(self)
        self.icon_doubleclick_timer.setSingleShot(True)
        self.icon_doubleclick_timer.timeout.connect(self.icon_doubleclick_timeout)

    def create_actions(self):
        """Create actions and connect relevant signals"""
        self.startAction = QtGui.QAction(self.tr("&Start"), self)
        self.startAction.triggered.connect(self.vpn_start)
        self.stopAction = QtGui.QAction(self.tr("S&top"), self)
        self.stopAction.triggered.connect(self.vpn_stop)
        self.settingsAction = QtGui.QAction(self.tr("S&ettings ..."), self)
        self.settingsAction.triggered.connect(self.settings)
        self.logsAction = QtGui.QAction(self.tr("Show &logs ..."), self)
        self.logsAction.triggered.connect(self.logs)
        self.quitAction = QtGui.QAction(self.tr("&Quit"), self)
        self.quitAction.triggered.connect(self.quit)

    def create_menu(self):
        """Create menu and add items to it"""
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.startAction)
        self.trayIconMenu.addAction(self.stopAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.settingsAction)
        self.trayIconMenu.addAction(self.logsAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

    def create_icon(self):
        """Create system tray icon"""
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.iconActive = QtGui.QIcon("{}/openvpn.svg".format(os.path.dirname(os.path.abspath(__file__))))
        self.iconDisabled = QtGui.QIcon("{}/openvpn_disabled.svg".format(os.path.dirname(os.path.abspath(__file__))))
        self.trayIcon.activated.connect(self.icon_activated)
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.setIcon(self.iconDisabled)
        self.trayIcon.setToolTip("QOpenVPN")
        self.trayIcon.show()

    def update_status(self, disable_warning=False):
        """Update GUI according to OpenVPN status"""
        settings = QtCore.QSettings()
        vpn_status = self.vpn_status()
        if vpn_status:
            self.trayIcon.setIcon(self.iconActive)
            self.startAction.setEnabled(False)
            self.stopAction.setEnabled(True)
            self.vpn_enabled = True
        else:
            self.trayIcon.setIcon(self.iconDisabled)
            self.startAction.setEnabled(True)
            self.stopAction.setEnabled(False)

            if not disable_warning and settings.value("show_warning", type=bool) and self.vpn_enabled:
                QtGui.QMessageBox.warning(self, self.tr("QOpenVPN - Warning"),
                                          self.tr("You have been disconnected from VPN!"))
            self.vpn_enabled = False

    def systemctl(self, command, disable_sudo=False):
        """Run systemctl command"""
        settings = QtCore.QSettings()
        cmdline = []
        if not disable_sudo and settings.value("use_sudo", type=bool):
            cmdline.append(settings.value("sudo_command") or "sudo")
        cmdline.extend(["systemctl", command, "{}@{}".format(settings.value("service_name"), settings.value("vpn_name"))])
        return subprocess.call(cmdline)

    def vpn_start(self):
        """Start OpenVPN service"""
        retcode = self.systemctl("start")
        if retcode == 0:
            self.update_status()

    def vpn_stop(self):
        """Stop OpenVPN service"""
        retcode = self.systemctl("stop")
        if retcode == 0:
            self.update_status(disable_warning=True)

    def vpn_status(self):
        """Check if OpenVPN service is running"""
        retcode = self.systemctl("is-active", disable_sudo=True)
        return True if retcode == 0 else False

    def settings(self):
        """Show settings dialog"""
        dialog = QOpenVPNSettings(self)
        if dialog.exec_() and self.vpn_enabled:
            self.vpn_stop()
            self.vpn_start()

    def logs(self):
        """Show log viewer dialog"""
        dialog = QOpenVPNLogViewer(self)
        dialog.exec_()

    def icon_activated(self, reason):
        """Start or stop OpenVPN by double-click on tray icon"""
        if reason == QtGui.QSystemTrayIcon.Trigger or reason == QtGui.QSystemTrayIcon.DoubleClick:
            if self.icon_doubleclick_timer.isActive():
                self.icon_doubleclick_timer.stop()
                if self.vpn_enabled:
                    self.vpn_stop()
                else:
                    self.vpn_start()
            else:
                self.icon_doubleclick_timer.start(QtGui.qApp.doubleClickInterval())

    def icon_doubleclick_timeout(self):
        """Action performed after single-click on tray icon"""
        pass

    def quit(self):
        """Quit QOpenVPN GUI (and ask before quitting if OpenVPN is still running)"""
        if self.vpn_enabled:
            reply = QtGui.QMessageBox.question(
                self, self.tr("QOpenVPN - Quit"),
                self.tr("You are still connected to VPN! Do you really want to quit "
                        "QOpenVPN GUI (OpenVPN service will keep running in background)?"),
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No
            )
            if reply == QtGui.QMessageBox.Yes:
                QtGui.qApp.quit()
        else:
            QtGui.qApp.quit()


def main():
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName("QOpenVPN")
    app.setOrganizationDomain("qopenvpn.eutopia.cz")
    app.setApplicationName("QOpenVPN")
    app.setQuitOnLastWindowClosed(False)
    window = QOpenVPNWidget()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
