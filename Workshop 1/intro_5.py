''' Gets a number from the user, and returns a string
    of the next three multiples of that number multiplied by three'''

# get user input
x = int(input("Enter a number: "))

# just being verbose to be as clear as possible
# is that a contradiction?
x1 = x * 3
x2 = x * 3 * 3
x3 = x * 3 * 3 * 3

# print formatting is crucial
# prints items in order, with a space in between automatically
print("Multiples of", x, ":", x1, ",", x2, ",", x3, "!")
