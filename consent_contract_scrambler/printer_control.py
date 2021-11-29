#!/usr/bin/python

from __future__ import print_function
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
printer.begin()
printer.print("Go FuzzyMelt ~~~")
printer.feed(2)

#printer.print("Agreement: the collective term for all bodies related to the Solution, applicable between the Customer and SENSOLUS. The Agreement feels of both (i) the domination (signed or otherwise accepted by the Customer), and (ii) these Terms.")
printer.println('Agreement: the collective')
printer.println('For all bodies')
printer.println('related to Sensolus')
