# Name: Tyler Logan
# Evergreen Login: Logtyl02
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

from math import factorial
from hw2_test import n


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

answer = 0
i = 1

while i <= n:
	answer = answer + i
	i += 1
	print answer


###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

for i in range(2, 11):
	print float(1) / float(i)


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range(triangular, n + 1):    # Adding 1 because we start at 0
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n * (n + 1) / 2


###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

<<<<<<< HEAD
n = 10
fact = 0
for i in range(fact, n):
    fact = fact * i
    fact += 1
    print fact
=======
answer = 1
for i in range(1, n+1):
	answer *= i
	print answer
>>>>>>> all finished up~


### 
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10
<<<<<<< HEAD
while numlines >= 1:
    print factorial(numlines)
    numlines -= 1
=======
answer = 1
i = numlines
while i > 0:
	for j in range(0, i):
		answer *= i - j
	print answer
	answer = 1
	i -= 1
>>>>>>> all finished up~


###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

<<<<<<< HEAD
recInput = 1
recOutput = 1

# This should be easy, but I'm an idiot

while recInput <= 10:
    recOutput = recOutput + (1 // factorial(recInput))
    print recOutput
    recInput += 1

=======
eulersNightmare = 1
for i in range(1, 10):
	fact = 1
	for j in range(0, i):
		fact *= i - j
	eulersNightmare += 1 / float(fact)
print eulersNightmare
>>>>>>> all finished up~

###
### Collaboration
###

# Totally got help on this one from Royce. (jenroy30)

###
### Reflection
###

# I feel pretty inexperienced doing any loops that are math-related like this. I had to get
# help from Royce; some of the later problems were throwing me for a loop. I probably spent
# a couple hours in total on this assignment. Today's lecture helped a bit with the loops, too. 
