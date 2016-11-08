''' Write a loop that returns the sum of the next ten numbers of a seed number.
Test Suite:
inputs:		output:		domain:
3		1 3 		Positive Integers
0				Zero (border case)
-5				We won't deal with these either, lol '''


# Getting a number from the user
num = int(input("Enter a number:"))

# Start at 1, step by 2, go until just below (num + 1)
for i in range(1, num + 1, 2):
	print(i)

''' A more naive solution:
for i in num:
	if i % 2 == 1:
		print(i) '''
