''' Gets two numbers from the user, and returns the second value
    subtracted from the first '''

# Get two integers from the user
firstNumber = int(input("First number? ")) # conversion from str -> int
secondNumber = int(input("Second number? "))

# find their difference
result = firstNumber - secondNumber

# print the result (convert int -> str)
print("The answer is ", result)
