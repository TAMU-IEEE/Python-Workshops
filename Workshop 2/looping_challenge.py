'''Write a loop that prints out the Fibonacci number entered by the user.
This is the OEIS sequence # A000045
Test Suite:
inputs:		output:				domain:
3			0 1 1 				third term of Fibonacci sequence
0								zeroth term as we define it, is null'''

# get user input
term = int(input("Enter a term:"))

# initial conditions
a = 0
b = 1

# iterate over sequence until term-th term
for i in range(0, term):
	print(a)
	
	# a is the next term
	# this is definition of fibonacci: F(n) = (n-1) + (n-2)
	a = a + b
	# swap the terms (remember this?)
	a, b = b, a
	'''
	you can also swap them like this:
	c = a
	a = b
	b = c
	
	OR:
	a = a ^ b
	b = a ^ b
	a = a ^ b
	'''