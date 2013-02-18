#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from distutils.core import setup
from qopenvpn import version

setup(name = "QOpenVPN",
      version = version.__version__,
      description = "Simple OpenVPN GUI written in PyQt for systemd based distributions",
      author = "Michal Krenek (Mikos)",
      author_email = "m.krenek@gmail.com",
      url = "https://github.com/xmikos/qopenvpn",
      license = "GNU GPLv3",
      packages = ["qopenvpn"],
      package_data = {"qopenvpn": ["openvpn.svg", "openvpn_disabled.svg"]},
      data_files = [("share/applications", ["qopenvpn.desktop"]),
                    ("share/pixmaps", ["qopenvpn.png"])],
      scripts = ["scripts/qopenvpn"],
      requires = ["PyQt4"],
)
