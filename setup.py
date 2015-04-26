#!/usr/bin/env python

from setuptools import setup
from qopenvpn.version import __version__

setup(
    name="QOpenVPN",
    version=__version__,
    description="Simple OpenVPN GUI written in PyQt for systemd based distributions",
    author="Michal Krenek (Mikos)",
    author_email="m.krenek@gmail.com",
    url="https://github.com/xmikos/qopenvpn",
    license="GNU GPLv3",
    packages=["qopenvpn"],
    package_data={
        "qopenvpn": [
            "openvpn.svg",
            "openvpn_disabled.svg",
            "*.ui",
            "languages/*.qm",
            "languages/*.ts"
        ]
    },
    data_files=[
        ("share/applications", ["qopenvpn.desktop"]),
        ("share/pixmaps", ["qopenvpn.png"])
    ],
    entry_points={
        "gui_scripts": [
            "qopenvpn=qopenvpn.__main__:main"
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Security :: Cryptography",
        "Topic :: System :: Networking"
    ]
)
