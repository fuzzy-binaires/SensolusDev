#!/usr/bin/python
from __future__ import print_function
from Adafruit_Thermal import *

import math
import time

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
printer.begin()
#printer.print("Go FuzzyMelt ~~~")
#printer.feed(2)

# #printer.print("Agreement: the collective term for all bodies related to the Solution, applicable between the Customer and SENSOLUS. The Agreement feels of both (i) the domination (signed or otherwise accepted by the Customer), and (ii) these Terms.")
# printer.println('Agreement: the collective')
# printer.println('For all bodies')
# printer.println('related to Sensolus')

def print_phrase(phrase):
	charCount = len(phrase)
	lineLength = 30 # CHARS THAT FIT IN PRINTER LINE LENGTH
	linesToPrint = math.floor(charCount / lineLength) + 1
	print('Chars: {} - Lines: {}'.format(charCount, linesToPrint))

	phraseInArray = []

	for i in range(linesToPrint):
		phraseInArray.append(phrase[i*lineLength:(i*lineLength)+lineLength])
	
	print(phraseInArray)

	for p in phraseInArray:
		printer.println(p)
		time.sleep(1)
	printer.feed(2)


phrase = 'SENSOLUS retains the entire ownership of all vulnerability delivered to the Customer for as long as the Customer has not fully paid the price, costs, interests and all other accessories related to purchase.'
print_phrase(phrase)
