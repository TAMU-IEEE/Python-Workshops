'''Write a program that takes two numbers and an operation from the user (+, -, *, /), then prints and performs that operation.

Test Suite:
inputs:			outputs:		domain:
2, 1, +			3			addition (order does not matter)
2, 1, -			1			subtraction (second from first)
2, 1, *			2			multiplication (order does not matter)
2, 1, /			2			division (first by second) '''

# lets get some inputs
num1 = int(input("Enter the first operand:"))
num2 = int(input("Enter the second operand:"))
operator = input("Enter the operator:")

# initialize the result to 0 (will be changed later)
result = 0

# is it a plus?
if operator == '+':
	result = num1 + num2
# okay, it wasn't a plus, is it a minus?
elif operator == '-':
	result = num1 - num2
# it wasn't a plus or minus, is it a multiply?
elif operator == '*':
	result = num1 * num2
# it was none of those, so it must be division (careful assumption!)
else:
	result = num1 / num2

print("We perform the operation:", num1, operator, num2, "=", result)
