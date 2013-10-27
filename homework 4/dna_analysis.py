# Name: Tyler Logan
# Evergreen Login: logtyl02
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0
seq_length = len(seq)

for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0
g_count  = 0
c_count  = 0
a_count  = 0
t_count  = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
        if bp == 'C':
            c_count +=1
        elif bp == 'G':
            g_count +=1
    elif bp == 'A' or bp == 'T':
        # increment the count of at
        at_count = at_count + 1
        if bp == 'A':
            a_count +=1
        elif bp == 'T':
            t_count +=1


seq_length = len(seq)
sum_count = g_count + c_count + a_count + t_count

# divide the gc_count by the total_count
gc_content = float(g_count + c_count) / sum_count
at_content = float(a_count + t_count) / sum_count

# calculate the ratio of AT and GC pairs
ATGC_ratio = float(a_count + t_count) / (g_count + c_count)   
GC_High = False
GC_Low  = False

if gc_content >= .60:
    GC_High = True
    GC_Low  = False
elif gc_content <= .40:
    GC_High = False
    GC_Low  = True    


# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'G Count:', g_count
print 'C Count:', c_count
print 'A count:', a_count
print 'T count:', t_count
print 'Sum count:', sum_count     # Count of all the relevant characters (G, C, A, and T)
print 'Total Count:', total_count # Total count of characters in the file, including garbage (Not G, C, A, or T)
print 'seq length:', seq_length
print 'AT/GC Ratio:', ATGC_ratio

if GC_High == True:
    print 'GC Classification: High GC Content'
elif GC_Low == True:
    print 'GC Classification: Low GC Content'
elif GC_High == False and GC_Low == False:
    print 'GC Classification: Moderate GC Content'