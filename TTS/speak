#!/usr/bin/python

import sys
import pyvona
import subprocess

__author__ = "Shyam"

#print " ".join(sys.argv[1:])
subprocess.call(["amixer cset numid=3 1 > /dev/null 2> /dev/null"], shell=True)
v = pyvona.create_voice('GDNAJ3Z7P4V6SVWR3TJQ', 'V53YvHKZRmnr57/ZfcRMk/qfcRbHjFiq9jCrGDEG')
v.speak(" ".join(sys.argv[1:]))
