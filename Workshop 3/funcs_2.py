'''Write a function that returns two given strings in alphabetical order.
Test suite:
input:				output:				domain:
"hi", "man"			"hi man"			ordered
"zz", "aa"			"aa zz"				unordered '''

# think about how we compare characters and their hidden ascii value!
def alphabetizeMe(string1, string2):
    for i in range(0, len(string1)):
    	if string1[i] < string2[i]:
    		return '{0} {1}'.format(string1, string2)
    	elif string2[i] < string1[i]:
    		return '{0} {1}'.format(string2, string1)

# it's possible that there is a more elegant solution
print(alphabetizeMe('rocks', 'oneal'))
