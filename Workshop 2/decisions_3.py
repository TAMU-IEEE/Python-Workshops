'''Prints the absolute value of a number entered by the user.

Test Suite:
inputs:		outputs:	domain:
-3			3			Negative integers
0			0			Zero (border case)
9			9			Positive integers '''

number = int(input("Enter a number:"))

if number < 0:
	print("The absolute value is", number * -1)
else:
	print("The absolute value is", number)