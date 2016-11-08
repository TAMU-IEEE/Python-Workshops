''' Write a loop that returns the sum of the next ten numbers of a seed number.
Test Suite:
inputs:		output:		domain:
4		99 		Positive Integers
0		55		Zero (border case)
-5		0		Negative numbers '''


# Getting a number from the user
num = int(input("Enter a number:"))

sum = 0

# Start at number, go until ten more than number
for i in range(num, num + 11):
	sum += i
	
print(sum)
