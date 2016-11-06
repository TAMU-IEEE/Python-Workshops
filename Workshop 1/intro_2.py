''' Gets two numbers from the user, and returns the second value
    subtracted from the first, multiplied by 3 '''

# Get two integers from the user
firstNumber = int(input("First number? ")) # conversion from str -> int
secondNumber = int(input("Second number? "))

# find their difference, multiply by 3
# order of operations is important!
result = (firstNumber - secondNumber) * 3

# print the result (convert int -> str)
print("The answer is ", result)
