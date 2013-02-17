#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from distutils.core import setup
from qopenvpn import version

setup(name = "QOpenVPN",
      version = version.__version__,
      description = "Simple OpenVPN GUI which uses systemd",
      author = "Michal Krenek",
      author_email = "m.krenek@gmail.com",
      url = "http://qopenvpn.eutopia.cz",
      license = "GNU GPLv3",
      packages = ["qopenvpn"],
      package_data = {"qopenvpn": ["openvpn.svg", "openvpn_disabled.svg"]},
      scripts = ["scripts/qopenvpn"],
      requires = ["PyQt4"],
)
