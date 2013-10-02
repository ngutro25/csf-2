# Name: Tyler Logan
# Evergreen Login: Logtyl02
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

# Quadratic Values

quadA = 1
quadB = -5.86
quadC = 8.5408


def quadratic(a, b, c):
	quadFirstAnswer = ((-b) + math.sqrt((b**2) - 4 * a * c )) / 2 * a
	quadSecondAnswer = ((-b) - math.sqrt((b**2) - 4 * a * c )) / 2 * a
	print "The first root is: "
	print quadFirstAnswer
	print "The second root is: "
	print quadSecondAnswer
	

quadratic(quadA, quadB, quadC)

###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test



a = hw1_test.a    # Setting the variables to something easier to type
b = hw1_test.b
c = hw1_test.c
d = hw1_test.d
e = hw1_test.e
f = hw1_test.f

print str(a)
print str(b)
print str(c)
print str(d)
print str(e)
print str(f)



###
### Problem 3
###

print "Problem 3 solution follows:"

print str((a and b) or (not c) and not (d or e or f))

###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").
