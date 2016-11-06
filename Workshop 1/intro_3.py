''' Gets two numbers from the user, and returns the remainder
    of dividing the second number by the first (Hint: %) '''

# Get two integers from the user
firstNumber = int(input("First number? ")) # conversion from str -> int
secondNumber = int(input("Second number? "))

# using our remainder operator, modulus
result = firstNumber % secondNumber

# print the result (convert int -> str)
print("The answer is ", result)
