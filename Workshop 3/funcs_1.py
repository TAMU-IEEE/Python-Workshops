'''Use the print formatter to print π (3.141592653589793) to the 8th decimal.

There is only one test case:
output:
3.14159265 '''

# going to use Python's math library
import math

# easy enough
print('{:1.8f}'.format(math.pi))
