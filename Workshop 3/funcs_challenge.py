'''Write a function that determines whether a given string 
   is a palindrome (can be read the same forwards and backwards)
   
   Test suite:
   input:				output:				domain:
   "redivider"			True				palindomes
   "onealio"			False				non-palindromes   '''

def isPalindrome(testString):
	result = ''
	# careful about structure of loop
	for n in range(len(testString) -1, -1, -1):
		result += testString[n]
	return testString == result
	
print('is racecar a palindrome?', isPalindrome('racecar'))
print('is Niagara, O Roar Again! a palindome?', isPalindrome('niagaraoroaragain'))
print('is hello a palindrome?', isPalindrome('hello'))
