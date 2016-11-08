''' Gets two numbers from the user and returns the larger number of the two.
Test Suite:
inputs:		output:		domain:
1, 2		2		Integers greater than 0
0, 0 		0		Integers that are equal (border case)
-1, 1		1		Integers less than 0 '''


# Getting a couple of numbers from the user
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

# Here is our conditional...
if num1 > num2: # If the first number is greater than the second,
	print("The larger number is", num1) # then print this number
else: # Otherwise... (notice we do not need to check the alternative condition)
	print("The larger number is", num2)
