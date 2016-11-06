'''Determines if a number entered by the user is even or odd'''

# you will never stop using this technique once you've learned it!
# it's really powerful

# get user input
x = int(input("A number to check for odd/even: "))

# use modulus to get the remainder when divided by 2
# every even number by definition can be split by 2
result = x % 2

# we could use an if statement here but we haven't learned that yet!
print("result: ", result, "\nIf the result is 0, then the number is even. If it is 1, the number is odd.")
