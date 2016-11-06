''' Read in two numbers from the user,
    and swap the contents of these numbers '''

# get two numbers from the user
num1 = int(input("First number = "))
num2 = int(input("Second number = "))

# we need to hold the contents of the first number
temp = num1

# go ahead and swap the first number
num1 = num2

# retrieve our stored value of the first number
num2 = temp

# they are now swapped
print("Num1 is now:", num1, "\nNum2 is now:", num2)


# BONUS: You don't need to know this... but
# a fancier way of doing this (and efficient, but rather low level)

# let's swap them back without using temp

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print("\nUsing XOR to sawp them back...\nNum1 is now:", num1, "\nNum2 is now:", num2)
