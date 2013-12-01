# Author: Tyler Logan
# Evergreen State College
#
# This is an assembler for my computer science course's SAM
# Create Machine Code from Assembly Instructions

from datetime import datetime
import logging
import sys

COMMENT_CHARS = ['#', '//']
INSTRUCTION_WIDTH = 8 # Bits
MEMORY = 128

# SAM OP Codes

LDA_bin = '0000' # Load
ADD_bin = '0001' # Addition
SUB_bin = '0010' # Subtraction
STA_bin = '0011' # Store
JMP_bin = '0100' # Jump
JAZ_bin = '0101' # Comparative Conditions Met
HLT_bin = '1111' # STAHP

OPCODES = {'LDA':'0000',
		   'ADD':'0001',
		   'SUB':'0010',
		   'STA':'0011',
		   'JMP':'0100',
		   'JAZ':'0101',
		   'OUT':'1110',
		   'HLT':'1111',
			}

# Hex Locations

LDA_hex = '0D' = Mem_Loc_0
ADD_hex = '1E' = Mem_Loc_1
SUB_hex = '2F' = Mem_Loc_2
OUT_hex = 'E0' = Mem_Loc_3
HLT_hex = 'F0' = Mem_Loc_4

Mem_Loc_15 = '02'
Mem_Loc_14 = '07'
Mem_Loc_13 = '04'


def main(argv = None):
	if argv == None:
		argv = sys.argv

	# Exit if args != 3
	# There should be 3 arguments: self, input file, and output file
	if len(sys.argv) != 3:
		print >>sys.stderr, 'Syntax: python sam_assembler.py infile outfile'
		return 2

	# Exit if args equal each other (would overwrite input file)
	if argv[1] == argv[2]:
		print >>sys.stderr, 'Error: Input and output filenames are the same'
		return 2

	# Check if the file exists, and if it does, open it
	if fileExists(argv[1]):
		inFile = open(argv[1], 'r')
		print 'Hooray! You successfully opened a file!' % (argv[1])
	else:
		print >>sys.stderr, 'Error: You gave me a crappy file, you jerk'

	lineNum = 0
	instructions = []
	valid = True

	for line in inFile:
		lineNum += 1

		# Remove comments from line
		newLine = removeComments(line, COMMENT_CHARS)
		# If the stripped line is now empty, skip it
		newLine = newLine.strip()
		if (newLine == ''):
			continue

		# Lowercase the line
		newLine = newLine.lower()
		# Split the line into seperate elements
		splitLine = newLine.split()
		lineElements = len(splitLine)

		# Process line based on number of elements
		if lineElements == 1:
			success = processOneElement(splitLine[0], len(instructions)), lineNum)
			valid = valid and success
		elif lineElements == 2:
			result = processTwoElements(splitLine, lineNum)
			if result == None:
				valid = False
			else:
				instructions.append(result)
		elif lineElements == 4:
			result = processFourElements(splitLine, lineNum)
			if result == None:
				valid = False
			else:
				instructions.append(result)
		else:
			logging.error('%d: Could not parse instruction - invalid number of elements' % lineNum)
			valid = False
	inFile.close()
