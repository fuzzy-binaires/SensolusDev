#!/usr/bin/python
from __future__ import print_function
from Adafruit_Thermal import *
import math
import time

printer = None
lineLength = 30 # CHARS THAT FIT IN PRINTER LINE LENGTH

def initialize():
	printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
	printer.begin()

def print_phrase(phrase):

	# PRINTER WORKS IF GIVEN EACH LINE SEPARATELY, WITH A DELAY IN BETWEEN
	# SO, LET'S CUT THE PHRASES APPROPIATELY
	
	#lineLength = 30 # CHARS THAT FIT IN PRINTER LINE LENGTH
	charCount = len(phrase)
	linesToPrint = math.floor(charCount / lineLength) + 1 # LINES NEEDED TO FIT ALL CHARS
	#print('Chars: {} - Lines: {}'.format(charCount, linesToPrint))

	phraseInArray = []

	# CROP THE PHRASE EVERY 30 CHARS AND ADD TO ARRAY
	for i in range(linesToPrint):
		phraseInArray.append(phrase[i*lineLength:(i*lineLength)+lineLength])
	
	#print(phraseInArray)

	# SEND TO PRINT, WITH PAUSES, AND THEN LEAVE 2 BLANK LINES
	for p in phraseInArray:
		printer.println(p)
		time.sleep(0.5)
	printer.feed(1)
	printer.println('================')
	printer.feed(2)


#phrase = 'SENSOLUS retains the entire ownership of all vulnerability delivered to the Customer for as long as the Customer has not fully paid the price, costs, interests and all other accessories related to purchase.'
#print_phrase(phrase)
