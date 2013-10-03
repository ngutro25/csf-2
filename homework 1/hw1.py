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
import hw1_test
import subprocess

answers = []

###
### Problem 1
###

print "\nProblem 1 solution follows:"

# Quadratic Values

quadA = 1
quadB = -5.86
quadC = 8.5408


def quadratic(a, b, c):
	quadFirstAnswer = ((-b) + math.sqrt((b**2) - 4 * a * c )) / 2 * a
	quadSecondAnswer = ((-b) - math.sqrt((b**2) - 4 * a * c )) / 2 * a
	print 'The first root is: ' + str(quadFirstAnswer) + '\nThe second root is: ' + str(quadSecondAnswer)
	answers.append(quadFirstAnswer)
	answers.append(quadSecondAnswer)
	
quadratic(quadA, quadB, quadC)

###
### Problem 2
###

print "\nProblem 2 solution follows:"

a = hw1_test.a    # Setting the variables to something easier to type
b = hw1_test.b
c = hw1_test.c
d = hw1_test.d
e = hw1_test.e
f = hw1_test.f

probTwoList = [a, b, c, d, e, f]

for i in probTwoList:
    print i
    answers.append(i)

###
### Problem 3
###

print "\nProblem 3 solution follows:"

problemThreeAns = ((a and b) or (not c) and not (d or e or f))
print str(problemThreeAns)

answers.append(problemThreeAns)

###
### Problem 4
###

# Opens or creates a new text file and places each answer into it on a new line
fo = open('csf/homework 1/outputs.txt', 'wb')
for i in answers:
    fo.write(str(i))
    fo.write('\n')
fo.close

subprocess.Popen('diff outputs.txt answers.txt')

###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").
