#!/usr/bin/python

import sys
import subprocess

__author__ = "Shyam"

var=sys.argv[1]
subprocess.call(["amixer cset numid=3 1 > /dev/null 2> /dev/null"], shell=True)
subprocess.call(["pico2wave -w test.wav var"] , shell=True)
subprocess.call(["aplay test.wav"], shell=True)
