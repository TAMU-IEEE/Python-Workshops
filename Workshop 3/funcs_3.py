'''Write a function that sings the song "99 Bottles of Beer" with n number of bottles to start'''

# we implement this iteratively
def singBottles(bottles):
	for n in range(bottles, -1, -1):
		if n == 0:
			print('{:^100}'.format('No more bottles of beer on the wall, no more bottles of beer.'))
			print('{:^100}'.format('Go to the store and buy some more, {0} bottles of beer on the wall.'.format(bottles)))
		else:
			print('{:^100}'.format('{0} bottles of beer on the wall, {0} bottles of beer. '.format(n, n - 1)))
			print('{:^100}'.format('Take one down and pass it around, {1} bottles of beer on the wall.'.format(n, n - 1)))
					  

# recursively!
def recSingBottles(bottles):
	if bottles == 0:
		return '\nNo more bottles of beer on the wall, no more bottles of beer.'.format(bottles)
	return '\n{0} bottles of beer on the wall, {0} bottles of beer. ' \
		   '\nTake one down and pass it around, {1} bottles of beer on the wall.'.format(bottles, bottles - 1) \
		   + recSingBottles(bottles - 1)
	
print('Iterative implementation:')
singBottles(3)
print('\n\nRecursive implementation (any differences?):\n', recSingBottles(3))
