'''Write a loop that prints out every natural number that is divisible by 7 and less than 30.
Test Suite:
inputs:		output:				domain:
none		0 7 14 21 28 			divisible by 7 and less than 30'''


# don't need any input, which makes this practically a calculator
for i in range(0, 30):
	if i % 7 == 0:
		print(i)
