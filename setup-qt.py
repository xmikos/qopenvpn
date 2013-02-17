#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
from glob import glob

package = "qopenvpn"
module = "qopenvpn"

print "Rebuilding PyQt resource files..."
for f in glob('%s/*.qrc' % package):
    os.system('pyrcc4 -o %s/qrc_%s.py %s' % (package, os.path.basename(f[:-4]), f))

print "Rebuilding PyQt UI files..."
for f in glob('%s/*.ui' % package):
    os.system('pyuic4 -o %s/ui_%s.py %s' % (package, os.path.basename(f[:-3]), f))

print "Updating translations..."
os.system('pylupdate4 %s/*.py -ts %s/%s.ts' % (package, package, module))
os.system('lrelease %s/%s.ts' % (package, module))

print "Regenerating .pyc files..."
for f in glob('%s/*.pyc' % package):
    os.remove(f)
__import__("%s.%s" % (package, module))
