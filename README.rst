QOpenVPN
========

Simple OpenVPN GUI written in PyQt for systemd based distributions

Requirements
------------

- Python >= 3.3
- PyQt >= 4.5
- OpenVPN
- systemd with journald
- sudo and/or kdesu

Usage
-----

If you want to use systemctl without password prompt, you should add this line to /etc/sudoers (use visudo command for it)::

    %wheel ALL=(ALL) NOPASSWD: /usr/bin/systemctl

And then add yourself to wheel group::

    gpasswd -a your_username wheel

An alternative is to use kdesu instead of sudo (set this in QOpenVPN settings), but then you have to use password for every operation.

You should also add yourself to adm group for log viewer to work::

    gpasswd -a your_username adm
