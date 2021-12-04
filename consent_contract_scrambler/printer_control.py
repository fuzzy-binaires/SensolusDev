#!/usr/bin/python
from __future__ import print_function
from .Adafruit_Thermal import *
import math
import time

lineLength = 20 # CHARS THAT FIT IN PRINTER LINE LENGTH
zigzagBlockIndex = 0;

def initialize():
	global printer
	printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
	printer.begin(200) # heat setting 0-255-darkest
	printer.setTimes(26000,2100) # MicroSecs for printOneScanline,feedOneBlankScanline
	#zigzagBlockIndex = 0

def format_text_block( phrases, type):
	# FORMATTING TEXT IF USING ~20 CHARACTERS PER LINE (INSTEAD OF THE FULL 30 CHARS PER WIDTH)
	formattedPhrases = []
	indent = 2
	global zigzagBlockIndex
	
	if type == 'centered':
		for p in phrases:
			formattedPhrases.append((' '*6) + p) ## ADD 8 SPACE BEFORE ALL PHRASES
		print('Text format: Centered')
		return formattedPhrases
	elif type == 'zigzag-phrase':
		# ZIG-ZAG: ADD INDENTATION, OR DOUBLE INDENT
		for i,value in enumerate(phrases): # enumerate let's me get the array's index value, and the value
			if i%2 == 0:
				formattedPhrases.append((' '*indent) + value)
			else:
				formattedPhrases.append((' '*(indent*6)) + value)
		print('Text format: ZigZag')
		return formattedPhrases
	elif type == 'zigzag-block':
                for p in phrases:
                        if zigzagBlockIndex % 2 == 0:
                                formattedPhrases.append((' '*indent) + p)
                        else:
                                formattedPhrases.append((' '*indent*4) + p)
                zigzagBlockIndex += 1
                return formattedPhrases
	else:
		print('Text format: No modification')
		return phrases


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
	
	print(phraseInArray)
	print('--')

	formatted_phrases = format_text_block(phraseInArray, 'centered')
	print(formatted_phrases)

	# SEND TO PRINT, WITH PAUSES, AND THEN LEAVE 2 BLANK LINES
	for p in formatted_phrases:
                printer.println(p)
                time.sleep(1)
	#printer.feed(1)
	#printer.println('====')
	printer.feed(3)


#phrase = 'SENSOLUS retains the entire ownership of all vulnerability delivered to the Customer for as long as the Customer has not fully paid the price, costs, interests and all other accessories related to purchase.'
#print_phrase(phrase)
