'''Gets a number from the user, and prints “yes” if that number is divisible by
 4 or 7, and “no” otherwise.

Test Suite:
inputs:		outputs:	domain:
-7			"yes"		Negative factors
1			"no"		Positive integers, nonfactors
0			"no"		Zero (border case)
4			"yes"		Positive integers, factors of 4
7			"yes"		Positive integers, factors of 7
28			"yes"		Positive integers, factors of both (border case) '''

# Get input from the user
number = int(input("Enter a number to check:"))

# Conditionals
if number % 7 == 0:
	print("yes, because it is divisible by 7")
elif number % 4 == 0:
	print("yes,because it is divisible by 4")
else:
	print("no, it is not divisible by either 4 or 7")